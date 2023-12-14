def func(name: str, age: int, salary: float) -> str:
    print("Nmae", name)
    print("Age", age)
    print("Salary", salary)

    return "{} is {} years old and earns {} dollars per month".format(name, age, salary)
print(func("Taofeek", 30, 70000.00))
