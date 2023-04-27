import aiHarmDetection as api

testset = ["Today, I felt good in the morning; everything was good, but in the evening, it rained, and as a result, I got stuck in traffic. My life sucks; I should end it; I should kill myself.",
           "Today I felt good in the morning, everything was good, but in the evening, it rained, and as a result, I got stuck in the traffic; my life sucks",
           "i dont want to kill myself", "quiero morir", "i want to be hit by a running bus", "lol, if only i could just die"]

for test in testset:
    print(api.findResult(test))
    print("\n\n---------------------------------")


for test in testset:
    print(api.fullOutput(test))
    print("\n\n---------------------------------")