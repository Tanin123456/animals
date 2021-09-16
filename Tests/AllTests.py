from Tests.TestCases.AllAnimalsRun import AllAnimalsRun

tests = []
tests.append(AllAnimalsRun())

b = True
print("===============================================")
print()
for test in tests:
    if test.run:
        print(f"success: {test.description}")
    else:
        print(f"fail: {test.description}")
        b = False

print("\n\n===============================================")
if b:
    print("success")
else:
    print("FAILURE - TEST(S) FAILED")
print("===============================================")
print("")