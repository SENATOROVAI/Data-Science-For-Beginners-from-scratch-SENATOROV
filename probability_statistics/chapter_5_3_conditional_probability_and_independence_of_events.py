"""Conditional probability and independence of events."""

# +
# 1

p_val, s1, f1, s2, f2 = map(float, input().split())
test1, test2 = map(int, input().split())
if test1 == 1:
    prob_test1_b = s1
    prob_test1_n = f1
else:
    prob_test1_b = 1 - s1
    prob_test1_n = 1 - f1

if test2 == 1:
    prob_test2_b = s2
    prob_test2_n = f2
else:
    prob_test2_b = 1 - s2
    prob_test2_n = 1 - f2

prob_test_given_sick = prob_test1_b * prob_test2_b

prob_test_given_healthy = prob_test1_n * prob_test2_n

prob_sick = p_val

prob_healthy = 1 - p_val

prob_test_sick = prob_test_given_sick * prob_sick
prob_test_healthy = prob_test_given_healthy * prob_healthy

prob_test = prob_test_sick + prob_test_healthy

prob_b_given_test = (prob_test_given_sick * prob_sick) / prob_test

print(f"{prob_b_given_test:.5f}")

# +
# 2

M_val = int(input())
experiments = [tuple(map(int, input().split())) for _ in range(M_val)]

count_a = count_b = count_c = 0
count_ab = count_ac = count_bc = 0
count_abc = 0

for xa, xb, xc in experiments:
    if xa == 1:
        count_a += 1
    if xb == 1:
        count_b += 1
    if xc == 1:
        count_c += 1
    if xa == 1 and xb == 1:
        count_ab += 1
    if xa == 1 and xc == 1:
        count_ac += 1
    if xb == 1 and xc == 1:
        count_bc += 1
    if xa == 1 and xb == 1 and xc == 1:
        count_abc += 1

P_A = count_a / M_val
P_B = count_b / M_val
P_C = count_c / M_val
P_AB = count_ab / M_val
P_AC = count_ac / M_val
P_BC = count_bc / M_val
P_ABC = count_abc / M_val

is_ab_independent = abs(P_AB - P_A * P_B) < 1e-6
is_ac_independent = abs(P_AC - P_A * P_C) < 1e-6
is_bc_independent = abs(P_BC - P_B * P_C) < 1e-6

is_abc_independent = abs(P_ABC - P_A * P_B * P_C) < 1e-6

if is_ab_independent and is_ac_independent and is_bc_independent:
    if is_abc_independent:
        print("ALL_INDEPENDENT")
    else:
        print("PAIRWISE_ONLY")
else:
    print("NOT_INDEPENDENT")

# +
# 3

M_val, N_val, K_val = map(int, input().split())

training_data = []
for _ in range(M_val):
    training_data.append(list(map(int, input().split())))

test_data = []
for _ in range(N_val):
    test_data.append(list(map(int, input().split())))


spam_count = sum(1 for email in training_data if email[0] == 1)
non_spam_count = M_val - spam_count

p_spam = spam_count / M_val
p_non_spam = non_spam_count / M_val

p_feature_given_spam = []
for j_val in range(1, K_val + 1):
    count_feature_in_spam = sum(
        1 for email in training_data if email[0] == 1 and email[j_val] == 1
    )
    p_feature_given_spam.append(
        count_feature_in_spam / spam_count if spam_count > 0 else 0
    )

p_feature_given_non_spam = []
for j_val in range(1, K_val + 1):
    count_feature_in_non_spam = sum(
        1 for email in training_data if email[0] == 0 and email[j_val] == 1
    )
    p_feature_given_non_spam.append(
        count_feature_in_non_spam / non_spam_count if non_spam_count > 0 else 0
    )

results = []

for email in test_data:
    p_spam_given_features = p_spam
    for j_val in range(K_val):
        if email[j_val] == 1:
            p_spam_given_features *= p_feature_given_spam[j_val]
        else:
            p_spam_given_features *= 1 - p_feature_given_spam[j_val]

    p_non_spam_given_features = p_non_spam
    for j_val in range(K_val):
        if email[j_val] == 1:
            p_non_spam_given_features *= p_feature_given_non_spam[j_val]
        else:
            p_non_spam_given_features *= 1 - p_feature_given_non_spam[j_val]

    if p_spam_given_features == 0 and p_non_spam_given_features == 0:
        results.append(-1)
    elif p_spam_given_features > p_non_spam_given_features:
        results.append(1)
    elif p_spam_given_features < p_non_spam_given_features:
        results.append(0)
    else:
        results.append(-1)

print(" ".join(map(str, results)))
