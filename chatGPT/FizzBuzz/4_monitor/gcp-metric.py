from google.cloud import monitoring_v3
import time

client = monitoring_v3.MetricServiceClient()
project_name = client.project_path('your-gcp-project-id')

def fizzbuzz_function(request):
    start_time = time.time()
    
    # Your FizzBuzz logic here
    result = fizzbuzz_logic(request.args.get('number'))

    elapsed_time = time.time() - start_time

    series = monitoring_v3.types.TimeSeries()
    series.metric.type = 'custom.googleapis.com/fizzbuzz/execution_time'
    series.resource.type = 'global'
    series.metric.labels['function_name'] = 'fizzbuzz_function'
    point = series.points.add()
    point.value.double_value = elapsed_time
    point.interval.end_time.seconds = int(time.time())

    client.create_time_series(name=project_name, time_series=[series])

    return result
