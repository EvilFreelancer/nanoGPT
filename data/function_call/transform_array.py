def transform_array(data: list):
    result = []

    i = 0
    for item in data:
        if i == 0:
            role = "user"
            i = 1
        else:
            role = "assistant"
            i = 0
        content = item["content"]
        result.append({"role": role, "content": content})

    return result
