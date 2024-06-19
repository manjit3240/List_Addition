from multiprocessing import Pool

def add_numbers(numbers):
    return sum(numbers)

def perform_addition(request):
    numbers_list = request.payload

    if not all(isinstance(sublist, list) and all(isinstance(num, int) for num in sublist) for sublist in numbers_list):
        raise ValueError("All elements must be lists of integers")
    try:
        with Pool() as pool:
            result = pool.map(add_numbers, numbers_list)
    except Exception as ex:
        return "Error: "+str(ex)

    return result
