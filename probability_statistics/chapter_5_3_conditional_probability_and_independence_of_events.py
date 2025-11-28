"""Conditional probability and independence of events."""

# +
# 1


def main_1() -> None:  # pylint: disable=too-many-locals
    """Calculate posterior probability of disease using Bayes' theorem."""
    p1, s1, f1, s2, f2 = map(float, input().split())

    t1, t2 = map(int, input().split())

    p_t1_given_d1 = s1 if t1 == 1 else 1 - s1
    p_t2_given_d1 = s2 if t2 == 1 else 1 - s2

    p_t1_given_d0 = f1 if t1 == 1 else 1 - f1
    p_t2_given_d0 = f2 if t2 == 1 else 1 - f2

    like_d1 = p_t1_given_d1 * p_t2_given_d1
    like_d0 = p_t1_given_d0 * p_t2_given_d0

    num = like_d1 * p1
    den = num + like_d0 * (1 - p1)
    posterior = num / den if den > 0 else 0.0

    print(posterior)


if __name__ == "__main__":
    main_1()


# +
# 2

# fmt: off
# pylint: disable=too-many-locals

def check_independence(
    num_experiments: int, 
    data: list[tuple[int, int, int]]
) -> str:
    """Check pairwise and mutual independence of 3 events from experiments."""
    count_a = sum(a_var for a_var, _, _ in data)
    count_b = sum(b_var for _, b_var, _ in data)
    count_c = sum(c_var for _, _, c_var in data)

    count_ab = sum(a_var and b_var for a_var, b_var, _ in data)
    count_ac = sum(a_var and c_var for a_var, _, c_var in data)
    count_bc = sum(b_var and c_var for _, b_var, c_var in data)
    count_abc = sum(a_var and b_var and c_var for a_var, b_var, c_var in data)

    # Переводим в вероятности
    p_a = count_a / num_experiments
    p_b = count_b / num_experiments
    p_c = count_c / num_experiments

    p_ab = count_ab / num_experiments
    p_ac = count_ac / num_experiments
    p_bc = count_bc / num_experiments
    p_abc = count_abc / num_experiments

    pairs = [(p_ab, p_a * p_b), (p_ac, p_a * p_c), (p_bc, p_b * p_c)]
    pairwise = all(abs(lhs - rhs) < 1e-9 for lhs, rhs in pairs)

    mutual = abs(p_abc - p_a * p_b * p_c) < 1e-9

    if pairwise and mutual:
        return "ALL_INDEPENDENT"
    if pairwise:
        return "PAIRWISE_ONLY"
    return "NOT_INDEPENDENT"


def main_2() -> None:
    """Read input, run independence check, print result."""
    num_experiments = int(input().strip())
    data: list[tuple[int, int, int]] = []

    for _ in range(num_experiments):
        parts = input().split()
        if len(parts) != 3:
            raise ValueError("Each experiment must contain exactly 3 integers")
        a_smpl, b_smpl, c_smpl = map(int, parts)
        data.append((a_smpl, b_smpl, c_smpl))

    print(check_independence(num_experiments, data))


if __name__ == "__main__":
    main_2()

# +
# 3


def main_3() -> None:  # pylint: disable=too-many-locals
    """Classify emails with a naive Bayes model built from binary features."""
    m_train, n_test, n_features = map(int, input().split())

    train_labels: list[int] = []
    train_features: list[list[int]] = []
    for _ in range(m_train):
        row = list(map(int, input().split()))
        label = row[0]
        features = row[1:]
        train_labels.append(label)
        train_features.append(features)

    test_set: list[list[int]] = [list(map(int, input().split())) for _ in range(n_test)]

    count_spam: int = sum(train_labels)
    count_ham: int = m_train - count_spam

    prior_spam: float = count_spam / m_train
    prior_ham: float = count_ham / m_train

    prob_word_given_spam: list[float] = []
    prob_word_given_ham: list[float] = []
    for j_0 in range(n_features):
        ones_spam = sum(
            train_features[i][j_0] for i in range(m_train) if train_labels[i] == 1
        )
        ones_ham = sum(
            train_features[i][j_0] for i in range(m_train) if train_labels[i] == 0
        )
        prob_word_given_spam.append(ones_spam / count_spam if count_spam > 0 else 0.0)
        prob_word_given_ham.append(ones_ham / count_ham if count_ham > 0 else 0.0)

    results: list[int] = []
    eps: float = 1e-15

    for features in test_set:
        likelihood_spam: float = prior_spam
        for j_1, x_1 in enumerate(features):
            pj = prob_word_given_spam[j_1]
            likelihood_spam *= pj if x_1 == 1 else (1.0 - pj)

        likelihood_ham: float = prior_ham
        for j_2, x_2 in enumerate(features):
            pj = prob_word_given_ham[j_2]
            likelihood_ham *= pj if x_2 == 1 else (1.0 - pj)

        if likelihood_spam == 0.0 and likelihood_ham == 0.0:
            results.append(-1)
        elif abs(likelihood_spam - likelihood_ham) <= eps:
            results.append(-1)
        elif likelihood_spam > likelihood_ham:
            results.append(1)
        else:
            results.append(0)

    print(" ".join(map(str, results)))


if __name__ == "__main__":
    main_3()
