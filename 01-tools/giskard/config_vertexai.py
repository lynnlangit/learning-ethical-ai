"""
Vertex AI Configuration Template for Giskard

This module provides configuration utilities for integrating Giskard
with GCP Vertex AI models (Gemini, PaLM, etc.).

Usage:
    from config_vertexai import get_vertex_llm_client, get_giskard_model

    llm_client = get_vertex_llm_client()
    model = get_giskard_model(predict_fn, llm_client)
"""

import os
from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class VertexAIConfig:
    """Configuration for Vertex AI integration"""
    project_id: str
    location: str = "us-central1"
    model_name: str = "gemini-2.0-flash"
    temperature: float = 0.7
    max_output_tokens: int = 1024
    top_p: float = 0.95
    top_k: int = 40


def load_config_from_env() -> VertexAIConfig:
    """
    Load Vertex AI configuration from environment variables.

    Required environment variables:
        - GCP_PROJECT_ID: Your GCP project ID
        - GOOGLE_APPLICATION_CREDENTIALS: Path to service account JSON

    Optional environment variables:
        - GCP_REGION: Vertex AI region (default: us-central1)
        - VERTEX_MODEL: Model name (default: gemini-2.0-flash)

    Returns:
        VertexAIConfig: Configuration object

    Raises:
        ValueError: If required environment variables are missing
    """
    project_id = os.getenv("GCP_PROJECT_ID")
    if not project_id:
        raise ValueError(
            "GCP_PROJECT_ID environment variable is required. "
            "Set it with: export GCP_PROJECT_ID='your-project-id'"
        )

    credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    if not credentials_path:
        raise ValueError(
            "GOOGLE_APPLICATION_CREDENTIALS environment variable is required. "
            "Set it with: export GOOGLE_APPLICATION_CREDENTIALS='/path/to/key.json'"
        )

    return VertexAIConfig(
        project_id=project_id,
        location=os.getenv("GCP_REGION", "us-central1"),
        model_name=os.getenv("VERTEX_MODEL", "gemini-2.0-flash"),
        temperature=float(os.getenv("VERTEX_TEMPERATURE", "0.7")),
        max_output_tokens=int(os.getenv("VERTEX_MAX_TOKENS", "1024")),
    )


def get_vertex_llm_client(config: Optional[VertexAIConfig] = None):
    """
    Initialize Vertex AI LLM client for Giskard.

    Args:
        config: Optional VertexAIConfig. If None, loads from environment.

    Returns:
        VertexAIClient instance configured for Giskard

    Example:
        >>> client = get_vertex_llm_client()
        >>> response = client.complete("What is machine learning?")
    """
    try:
        from giskard.llm.client.vertexai import VertexAIClient
    except ImportError:
        raise ImportError(
            "Vertex AI support requires giskard[llm] extras. "
            "Install with: pip install 'giskard[llm]'"
        )

    if config is None:
        config = load_config_from_env()

    return VertexAIClient(
        model=config.model_name,
        project=config.project_id,
        location=config.location,
        generation_config={
            "temperature": config.temperature,
            "max_output_tokens": config.max_output_tokens,
            "top_p": config.top_p,
            "top_k": config.top_k,
        }
    )


def get_giskard_model(
    predict_function,
    llm_client,
    model_name: str = "Healthcare LLM",
    model_type: str = "text_generation",
    feature_names: Optional[List[str]] = None,
    description: str = ""
):
    """
    Wrap your model for Giskard compatibility.

    Args:
        predict_function: Callable that takes input and returns predictions
        llm_client: Vertex AI LLM client from get_vertex_llm_client()
        model_name: Human-readable model name
        model_type: One of: text_generation, classification, regression
        feature_names: List of input feature names
        description: Model description for reports

    Returns:
        giskard.Model instance ready for scanning

    Example:
        >>> def predict(df):
        ...     return df["query"].apply(lambda q: my_chatbot(q))
        >>>
        >>> client = get_vertex_llm_client()
        >>> model = get_giskard_model(predict, client, "Clinical Chatbot")
    """
    from giskard import Model

    return Model(
        model=predict_function,
        model_type=model_type,
        name=model_name,
        description=description,
        feature_names=feature_names or ["input"],
        llm_client=llm_client,
    )


def create_healthcare_dataset(
    queries: List[str],
    expected_responses: Optional[List[str]] = None,
    metadata: Optional[Dict] = None
):
    """
    Create a Giskard dataset for healthcare LLM testing.

    Args:
        queries: List of patient/clinical queries
        expected_responses: Optional list of ground truth responses
        metadata: Optional metadata (e.g., query categories, risk levels)

    Returns:
        giskard.Dataset instance

    Example:
        >>> queries = [
        ...     "What is the dosage for metformin in type 2 diabetes?",
        ...     "Should I stop taking my blood pressure medication?",
        ... ]
        >>> dataset = create_healthcare_dataset(queries)
    """
    import pandas as pd
    from giskard import Dataset

    data = {"query": queries}

    if expected_responses:
        data["expected_response"] = expected_responses

    if metadata:
        for key, values in metadata.items():
            data[key] = values

    df = pd.DataFrame(data)

    return Dataset(
        df=df,
        target=None,  # For generative models, target is optional
        name="Healthcare Test Queries",
        cat_columns=list(metadata.keys()) if metadata else []
    )


def configure_scan_features(
    include_hallucination: bool = True,
    include_bias: bool = True,
    include_privacy: bool = True,
    include_toxicity: bool = False,
    include_sycophancy: bool = True
) -> List[str]:
    """
    Configure which safety features to scan for.

    Args:
        include_hallucination: Detect medical misinformation
        include_bias: Detect demographic/clinical bias
        include_privacy: Check for PII leakage (HIPAA-relevant)
        include_toxicity: Check for harmful/toxic outputs
        include_sycophancy: Detect agreement with incorrect assumptions

    Returns:
        List of feature names for giskard.scan()

    Example:
        >>> features = configure_scan_features(include_toxicity=False)
        >>> scan(model, dataset, features=features)
    """
    features = []

    if include_hallucination:
        features.append("hallucination")
    if include_bias:
        features.extend(["bias", "fairness"])
    if include_privacy:
        features.extend(["privacy", "data_leakage"])
    if include_toxicity:
        features.append("toxicity")
    if include_sycophancy:
        features.append("sycophancy")

    return features if features else ["all"]


# Example usage and testing
if __name__ == "__main__":
    import sys

    print("🔧 Giskard Vertex AI Configuration Test")
    print("=" * 50)

    # Test 1: Load configuration
    try:
        config = load_config_from_env()
        print(f"✅ Configuration loaded successfully")
        print(f"   Project: {config.project_id}")
        print(f"   Region: {config.location}")
        print(f"   Model: {config.model_name}")
    except ValueError as e:
        print(f"❌ Configuration error: {e}")
        sys.exit(1)

    # Test 2: Initialize LLM client
    try:
        llm_client = get_vertex_llm_client(config)
        print(f"✅ Vertex AI client initialized")
    except Exception as e:
        print(f"❌ Client initialization failed: {e}")
        sys.exit(1)

    # Test 3: Test connection with simple prompt
    try:
        test_response = llm_client.complete(
            messages=[{"role": "user", "content": "Say 'Hello from Vertex AI' if you can read this."}],
            temperature=0.1
        )
        print(f"✅ Connection test successful")
        print(f"   Response: {test_response.message.content[:100]}...")
    except Exception as e:
        print(f"❌ Connection test failed: {e}")
        sys.exit(1)

    print("\n" + "=" * 50)
    print("✅ All configuration tests passed!")
    print("\nNext steps:")
    print("  1. Run: python healthcare_scan.py")
    print("  2. Check the generated HTML report")
    print("  3. Review 02-examples/01-giskard-quickstart.ipynb")
