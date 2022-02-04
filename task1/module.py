def individual_func(string):
    def replace_string(name, surname):
        nonlocal string
        answer = string.replace("%N%", name)
        answer = answer.replace("%F%", surname)
        return answer

    return replace_string
