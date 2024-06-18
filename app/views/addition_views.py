from multiprocessing import Pool

def add_numbers(numbers):
    return sum(numbers)

def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def perform_addition(request):
    numbers_list = request.payload
    flattened_list = flatten_list(numbers_list)

    if not all(isinstance(sublist, list) and all(isinstance(num, int) for num in sublist) for sublist in numbers_list):
        raise ValueError("All elements must be lists of integers")
    try:
        with Pool() as pool:
            result = pool.map(add_numbers, numbers_list)
    except Exception as ex:
        return "Error: "+str(ex)

    return result
