# Import data
training_set = pd.read_csv("data/training_set.csv", index_col=0)
test_set = pd.read_csv("data/test_set.csv", index_col=0)

# Select subset of data for dev
sub_training_set = training_set.iloc[:, 0:10]
sub_test_set = test_set.iloc[:, 0:8]


def generate_recommendations(train: pd.DataFrame, test: pd.Series) -> list:
    distances = [
        (lambda x, y: sum([abs(item[0] - item[1]) for item in zip(x, y)]))(val, test)
        for col, val in train.items()
    ]

    training_nn = train.iloc[:, distances.index(min(distances))].copy()
    training_nn.loc[test != 0] = 0

    recommendations = [0] * len(test_set)
    for item in list((-training_nn).argsort() + 1)[0:5]:
        recommendations[item] = 1

    return recommendations


res = [
    generate_recommendations(train=sub_training_set, test=sub_test_set[column])
    for column in sub_test_set
]
print(res)
