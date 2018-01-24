
def safe_float(obj):
    try:
        return float(obj)
    except (ValueError, TypeError) as e:
        print(e)
        return None

if __name__ == '__main__':
    print(safe_float('asdf'))