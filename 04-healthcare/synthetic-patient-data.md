# Synthetic Patient Data: Safe Generation for AI Testing

Best practices for generating realistic synthetic patient data for testing healthcare AI systems without compromising real patient privacy.

## Why Synthetic Patient Data?

**The Problem**: Testing healthcare AI requires realistic data, but using real patient data poses:
- HIPAA privacy risks (even de-identified data can be re-identified)
- Consent challenges (patients didn't consent to AI testing use)
- Limited diversity (real datasets often lack edge cases, rare conditions)
- Data scarcity (rare diseases, pediatric populations)

**The Solution**: Synthetically generated patient data that:
- ✅ Preserves clinical realism (correlations, distributions)
- ✅ Protects privacy (no linkage to real individuals)
- ✅ Enables extensive testing (edge cases, adversarial scenarios)
- ✅ Complies with HIPAA (not derived from real patients)

## Types of Synthetic Healthcare Data

```
┌────────────────────────────────────────────────────────┐
│        SYNTHETIC DATA GENERATION APPROACHES            │
├────────────────────────────────────────────────────────┤
│                                                        │
│  1. RULE-BASED                                         │
│     Hand-crafted templates + randomization             │
│     ⭐⭐⭐ Good for: Simple test cases                 │
│                                                        │
│  2. STATISTICAL MODELING                               │
│     Learn distributions from real data, sample new     │
│     ⭐⭐⭐⭐ Good for: Tabular clinical data          │
│                                                        │
│  3. GENERATIVE AI (GANs, VAEs, LLMs)                   │
│     Train models to generate realistic patients        │
│     ⭐⭐⭐⭐⭐ Good for: Complex, multimodal data     │
│                                                        │
│  4. HYBRID                                             │
│     Combine approaches for realism + control           │
│     ⭐⭐⭐⭐⭐ Good for: Production testing            │
│                                                        │
└────────────────────────────────────────────────────────┘
```

## Method 1: Rule-Based Synthetic Data (Quick Start)

### Use Case: Basic Testing of Clinical LLM

```python
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

# Template-based synthetic patient generator
def generate_synthetic_patient():
    """Generate a realistic synthetic patient record"""

    # Demographics
    gender = random.choice(["Male", "Female"])
    age = random.randint(18, 85)
    first_name = fake.first_name_male() if gender == "Male" else fake.first_name_female()
    last_name = fake.last_name()

    # Clinical conditions (realistic prevalence)
    conditions = []
    if age > 45 and random.random() < 0.3:  # 30% over 45 have hypertension
        conditions.append("Hypertension")
    if age > 50 and random.random() < 0.15:  # 15% over 50 have type 2 diabetes
        conditions.append("Type 2 Diabetes Mellitus")
    if random.random() < 0.05:  # 5% general population asthma
        conditions.append("Asthma")

    # Medications (correlated with conditions)
    medications = []
    if "Hypertension" in conditions:
        medications.append(random.choice(["Lisinopril 10mg daily", "Amlodipine 5mg daily"]))
    if "Type 2 Diabetes Mellitus" in conditions:
        medications.append("Metformin 1000mg twice daily")
    if "Asthma" in conditions:
        medications.append("Albuterol inhaler as needed")

    # Vital signs (realistic ranges)
    vitals = {
        "blood_pressure": f"{random.randint(110, 160)}/{random.randint(70, 100)}",
        "heart_rate": random.randint(60, 100),
        "temperature": round(random.uniform(97.0, 99.5), 1),
        "respiratory_rate": random.randint(12, 20),
        "oxygen_saturation": random.randint(95, 100)
    }

    # Lab results (if diabetic)
    labs = {}
    if "Type 2 Diabetes Mellitus" in conditions:
        labs["HbA1c"] = round(random.uniform(6.0, 9.0), 1)  # Diabetic range
        labs["fasting_glucose"] = random.randint(110, 200)

    return {
        "patient_id": f"SYNTH-{fake.uuid4()[:8].upper()}",  # Clearly synthetic
        "demographics": {
            "name": f"{first_name} {last_name}",
            "age": age,
            "gender": gender,
            "date_of_birth": (datetime.now() - timedelta(days=age*365)).strftime("%Y-%m-%d")
        },
        "conditions": conditions,
        "medications": medications,
        "vitals": vitals,
        "labs": labs
    }

# Generate test dataset
synthetic_patients = [generate_synthetic_patient() for _ in range(100)]

# Example usage
for patient in synthetic_patients[:3]:
    print(f"Patient: {patient['demographics']['name']}, Age {patient['demographics']['age']}")
    print(f"Conditions: {', '.join(patient['conditions']) or 'None'}")
    print(f"Medications: {', '.join(patient['medications']) or 'None'}")
    print(f"BP: {patient['vitals']['blood_pressure']}, HR: {patient['vitals']['heart_rate']}\n")
```

**Output Example**:
```
Patient: John Anderson, Age 62
Conditions: Hypertension, Type 2 Diabetes Mellitus
Medications: Amlodipine 5mg daily, Metformin 1000mg twice daily
BP: 145/88, HR: 78
```

## Method 2: LLM-Based Synthetic Patient Generation

### Use Case: Complex Clinical Narratives

```python
import vertexai
from vertexai.generative_models import GenerativeModel

vertexai.init(project="your-project-id", location="us-central1")
model = GenerativeModel("gemini-2.0-flash")

def generate_clinical_note(patient_template):
    """Generate realistic clinical note using LLM"""

    prompt = f"""Generate a realistic clinical progress note for a synthetic patient with these characteristics:

Age: {patient_template['age']}
Gender: {patient_template['gender']}
Conditions: {', '.join(patient_template['conditions'])}
Medications: {', '.join(patient_template['medications'])}

Include: Chief complaint, HPI, physical exam, assessment, and plan.
Make it clinically realistic but clearly synthetic (use placeholder names like "Patient A").
"""

    response = model.generate_content(prompt)
    return response.text

# Generate synthetic clinical note
patient = synthetic_patients[0]
clinical_note = generate_clinical_note(patient)
print(clinical_note)
```

**Example Output**:
```
CLINICAL PROGRESS NOTE

Patient: Patient A (Synthetic)
Age: 62, Gender: Male
Date: 2026-01-08

Chief Complaint: Follow-up for diabetes and hypertension

HPI: Patient A is a 62-year-old male with a history of type 2 diabetes mellitus
and hypertension presenting for routine follow-up. Reports good medication
compliance with metformin and amlodipine. No hypoglycemic episodes. Occasional
mild headaches, otherwise feels well.

Physical Exam:
- BP: 145/88 (slightly elevated)
- HR: 78, regular
- General: Well-appearing, no acute distress

Labs: HbA1c 7.2% (target <7%), fasting glucose 145 mg/dL

Assessment:
1. Type 2 DM - suboptimal control (HbA1c 7.2%)
2. Hypertension - BP slightly above target

Plan:
1. Increase metformin to 1500mg BID
2. Add lifestyle counseling (diet, exercise)
3. Recheck HbA1c in 3 months
4. Monitor BP, consider uptitrating amlodipine if remains elevated
```

## Method 3: Privacy-Preserving Synthetic Data (Differential Privacy)

### Use Case: Generating Synthetic Data FROM Real Data (Safely)

**Library**: SmartNoise SDK (Microsoft + OpenDP)

```python
# Example: Generate differentially private synthetic dataset
from smartnoise.synthesizers import DPCTGANSynthesizer
import pandas as pd

# Assume you have de-identified real data (still risky!)
real_patient_data = pd.read_csv("deidentified_patients.csv")

# Columns: age, gender, diagnosis_code, medication_count, hospitalization_count

# Train differentially private synthesizer
synthesizer = DPCTGANSynthesizer(
    epsilon=1.0,  # Privacy budget (lower = more private, less realistic)
    verbose=True
)

synthesizer.fit(real_patient_data, categorical_columns=["gender", "diagnosis_code"])

# Generate synthetic data with privacy guarantee
synthetic_data = synthesizer.sample(n=1000)

# ε=1.0 differential privacy ensures minimal privacy leakage
# Even if someone knows 999 of 1000 records, they learn minimal info about the 1000th
```

**When to Use**: When you MUST learn from real patient data but need formal privacy guarantees.

**Privacy-Utility Tradeoff**:
- ε < 1: Strong privacy, lower realism
- ε = 1-5: Balanced (recommended for healthcare)
- ε > 10: Weak privacy, higher realism

## Validation: Is Your Synthetic Data Realistic?

### Statistical Similarity

```python
from scipy.stats import ks_2samp

# Compare real vs synthetic data distributions
def validate_synthetic_data(real_data, synthetic_data):
    """Check if synthetic data matches real data distributions"""

    results = {}

    for column in real_data.columns:
        if real_data[column].dtype in ['int64', 'float64']:
            # Kolmogorov-Smirnov test (are distributions similar?)
            statistic, p_value = ks_2samp(real_data[column], synthetic_data[column])

            results[column] = {
                "p_value": p_value,
                "similar": p_value > 0.05  # If p>0.05, distributions are similar
            }

    return results

# Example
validation = validate_synthetic_data(real_patient_data, synthetic_data)
for col, result in validation.items():
    status = "✅ Similar" if result["similar"] else "❌ Different"
    print(f"{col}: {status} (p={result['p_value']:.3f})")
```

### Clinical Plausibility Checks

```python
def check_clinical_plausibility(synthetic_patients):
    """Validate synthetic data for clinical realism"""

    issues = []

    for patient in synthetic_patients:
        # Check 1: Age-appropriate conditions
        if patient['age'] < 25 and "Type 2 Diabetes Mellitus" in patient['conditions']:
            issues.append(f"Unlikely: {patient['patient_id']} has T2DM at age {patient['age']}")

        # Check 2: Medication-condition alignment
        if "Metformin" in str(patient['medications']) and "Diabetes" not in str(patient['conditions']):
            issues.append(f"Mismatch: {patient['patient_id']} on metformin without diabetes diagnosis")

        # Check 3: Vital sign ranges
        bp = patient['vitals']['blood_pressure']
        systolic = int(bp.split('/')[0])
        if systolic < 70 or systolic > 200:
            issues.append(f"Implausible BP: {patient['patient_id']} has BP {bp}")

    return issues

# Run validation
issues = check_clinical_plausibility(synthetic_patients)
if issues:
    print("⚠️ Clinical plausibility issues found:")
    for issue in issues:
        print(f"  - {issue}")
else:
    print("✅ All synthetic patients are clinically plausible")
```

## Privacy Risk: Can Synthetic Data Leak Real Patient Info?

### Membership Inference Attack

**Test**: Can an attacker determine if a specific real patient was in the training set?

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def membership_inference_test(real_data, synthetic_data, target_patient):
    """
    Test if synthetic data leaks information about specific real patients

    Returns:
        Risk score (0-1): Probability that target_patient is in training data
    """
    # Train a classifier to distinguish real vs synthetic
    real_data['label'] = 1  # Real
    synthetic_data['label'] = 0  # Synthetic

    combined = pd.concat([real_data, synthetic_data])
    X = combined.drop(['label'], axis=1)
    y = combined['label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)

    # Check if target patient is easily classified as "real"
    target_prob = clf.predict_proba([target_patient])[0][1]

    return target_prob  # Higher = more likely leaked

# Run test
target_patient_record = real_patient_data.iloc[0]
risk_score = membership_inference_test(real_patient_data, synthetic_data, target_patient_record)

if risk_score > 0.7:
    print(f"⚠️ HIGH PRIVACY RISK: Target patient identifiable (score={risk_score:.2f})")
else:
    print(f"✅ LOW PRIVACY RISK: Target patient not distinguishable (score={risk_score:.2f})")
```

## Best Practices for Healthcare Synthetic Data

### DO:
✅ **Clearly label as synthetic** (e.g., patient IDs starting with "SYNTH-")
✅ **Validate clinical plausibility** (age-condition correlations, med-diagnosis alignment)
✅ **Test privacy leakage** (membership inference, attribute inference)
✅ **Document generation method** (in data provenance logs)
✅ **Include edge cases** (rare conditions, adverse events, atypical presentations)
✅ **Use for testing only** (not for training clinical decision models without validation)

### DON'T:
❌ **Claim it's real** (always disclose synthetic nature)
❌ **Use for clinical decisions** (synthetic data doesn't replace real-world validation)
❌ **Ignore privacy risks** (even synthetic data can leak if poorly generated)
❌ **Skip clinical review** (have clinicians review sample for realism)
❌ **Forget to test edge cases** (common mistake: only generate "average" patients)

## Use Cases for Synthetic Patient Data

### 1. **LLM Safety Testing** (e.g., Giskard Scans)
```python
# Generate adversarial test cases
adversarial_patients = [
    generate_jailbreak_attempt(),  # Try to trick LLM
    generate_rare_disease(),       # Test handling of uncommon cases
    generate_conflicting_meds(),   # Test drug interaction detection
]

# Test LLM with synthetic scenarios
from giskard import scan
scan_report = scan(clinical_llm, synthetic_dataset)
```

### 2. **Bias Testing**
```python
# Generate patients across demographic groups
synthetic_cohorts = {
    "White, Male, 40s": generate_cohort(race="White", gender="Male", age_range=(40,49), n=100),
    "Black, Female, 40s": generate_cohort(race="Black", gender="Female", age_range=(40,49), n=100),
    "Hispanic, Male, 40s": generate_cohort(race="Hispanic", gender="Male", age_range=(40,49), n=100),
}

# Test if LLM treats cohorts differently
for cohort_name, patients in synthetic_cohorts.items():
    outcomes = [llm.predict(patient) for patient in patients]
    print(f"{cohort_name}: {analyze_treatment_recommendations(outcomes)}")
```

### 3. **Stress Testing**
```python
# Generate high-volume synthetic load
def stress_test_llm(llm, num_patients=10000):
    patients = [generate_synthetic_patient() for _ in range(num_patients)]
    start = time.time()
    for patient in patients:
        llm.predict(patient)
    duration = time.time() - start
    print(f"Processed {num_patients} patients in {duration:.1f}s ({num_patients/duration:.0f} patients/sec)")
```

### 4. **Training Data Augmentation** (Use with Caution)
```python
# Augment sparse real data with synthetic examples
real_rare_disease_cases = 50  # Limited real data
synthetic_rare_disease_cases = 500  # Augment with synthetic

# Combine for training (but validate on REAL held-out data)
combined_training_set = real_cases + synthetic_cases
model.train(combined_training_set)
model.test(real_held_out_test_set)  # Critical: Test on real data only
```

## Tools & Libraries

| Tool | Type | Use Case | Link |
|------|------|----------|------|
| **Faker** | Rule-based | Simple demographics, names, addresses | [GitHub](https://github.com/joke2k/faker) |
| **Synthea** | Patient simulator | Comprehensive EHR-style synthetic data | [Synthea.org](https://synthea.mitre.org/) |
| **SmartNoise** | Differential privacy | Privacy-preserving synthetic data | [GitHub](https://github.com/opendp/smartnoise-sdk) |
| **SDV** (Synthetic Data Vault) | ML-based | Tabular, time-series, relational data | [GitHub](https://github.com/sdv-dev/SDV) |
| **Gretel.ai** | Commercial | HIPAA-compliant synthetic data generation | [Gretel.ai](https://gretel.ai/) |

## Example: Full Synthetic Patient Generation Pipeline

```python
# Step 1: Generate synthetic cohort
from synthea import SyntheticPatientGenerator

generator = SyntheticPatientGenerator(
    population_size=1000,
    demographics_profile="US_2020_Census",
    conditions=["diabetes", "hypertension", "asthma"],
    time_range=("2020-01-01", "2026-01-01")
)

synthetic_cohort = generator.generate()

# Step 2: Validate plausibility
issues = check_clinical_plausibility(synthetic_cohort)
assert len(issues) == 0, f"Clinical plausibility errors: {issues}"

# Step 3: Test privacy leakage (if derived from real data)
if derived_from_real_data:
    privacy_risk = membership_inference_test(real_data, synthetic_cohort, target_patient)
    assert privacy_risk < 0.6, f"Privacy risk too high: {privacy_risk}"

# Step 4: Use for LLM testing
from giskard import scan
scan_report = scan(clinical_llm, synthetic_cohort)
print(f"Safety score: {scan_report.safety_score}")

# Step 5: Document provenance
metadata = {
    "generation_method": "Synthea + differential privacy",
    "privacy_budget": "ε=1.0",
    "clinical_validation": "Reviewed by 2 physicians",
    "use_cases": ["LLM safety testing", "Bias analysis"],
    "NOT_FOR": "Clinical decision-making, real patient care"
}
```

## Resources

### Synthetic Data Generation
- [Synthea Patient Simulator](https://synthea.mitre.org/)
- [SmartNoise SDK](https://github.com/opendp/smartnoise-sdk)
- [Synthetic Data Vault](https://github.com/sdv-dev/SDV)

### Privacy & Testing
- [Differential Privacy Introduction](https://programming-dp.com/)
- [Membership Inference Attacks](https://arxiv.org/abs/1610.05820)

### Healthcare AI Testing
- [Giskard Healthcare Testing](../01-tools/giskard/)
- [HIPAA Compliance](./hipaa-ai-checklist.md)
- [Clinical LLM Risks](./clinical-llm-risks.md)

---

**Key Takeaway**: Synthetic patient data is a powerful tool for safe AI testing, but must be generated carefully to ensure clinical realism and privacy protection. Always validate synthetic data with clinical experts and test on real data before deployment.
