# coding=utf-8

import numpy as np


class Bayes():
    def __init__(self, x, tags, test_x, **args):
        self.x = x
        self.tags = tags
        self.test_x = test_x

        if 'show' in args:
            show_flag = args['show']
        else:
            show_flag = False

        self.__result = self.__train()

        if show_flag:
            self.__show_probabilities()

    def __train(self):
        prior_probabilities, tag_index = self.__tags_process()
        conditional_probabilities = self.__conditional_probability(tag_index)

        posterior_probabilities = {}
        for tag, prior_probability in prior_probabilities.iteritems():
            probability = 1
            for dimension in conditional_probabilities[tag]:
                try:
                    probability = probability * \
                        conditional_probabilities[tag][dimension][self.test_x[dimension]]
                except KeyError as e:
                    probability = 0
                else:
                    pass
                finally:
                    pass
            posterior_probabilities[tag] = probability * prior_probability
        # print posterior_probabilities
        max_posterior_probability = max(
            posterior_probabilities.iteritems(), key=lambda x: x[1])
        tag = max_posterior_probability[0]

        self.__prior_probabilities = prior_probabilities
        self.__conditional_probabilities = conditional_probabilities
        self.__posterior_probabilities = posterior_probabilities

        return tag

    def __conditional_probability(self, tag_index):
        result = {}
        for tag, indexes in tag_index.iteritems():
            length = len(indexes)
            dimension_probalities = {}
            for dimension, line in enumerate(self.x):
                x_count = {}
                x_probability = {}
                for index in indexes:
                    if line[index] in x_count:
                        x_count[line[index]] = x_count[line[index]] + 1
                    else:
                        x_count[line[index]] = 1
                for value in x_count:
                    x_probability[value] = x_count[value] / float(length)
                dimension_probalities[dimension] = x_probability
            result[tag] = dimension_probalities
        # print result
        return result

    def __tags_process(self):
        tag_index = {}
        tag_count = {}
        for index, tag in enumerate(self.tags):
            if tag in tag_count:
                tag_count[tag] = tag_count[tag] + 1
                tag_index[tag].append(index)
            else:
                tag_count[tag] = 1
                tag_index[tag] = [index]
        # print tag_count
        length = len(self.tags)
        tag_probability = {}
        for tag in tag_count:
            tag_probability[tag] = tag_count[tag] / float(length)
        # print tag_probability
        # print tag_index
        return tag_probability, tag_index

    def __show_probabilities(self):
        print "prior probabilities:"
        for tag, p in self.__prior_probabilities.iteritems():
            print 'P(Y=' + str(tag) + ')=' + str(p)
        print "\nconditional_probabilities:"
        for tag in self.__conditional_probabilities:
            for dimension in self.__conditional_probabilities[tag]:
                strp = ""
                for value, p in self.__conditional_probabilities[tag][dimension].iteritems():
                    strp = strp + "P(X(" + str(dimension) + ")=" + \
                        str(value) + "|Y=" + str(tag) + ")=" + str(p) + "\t"
                print strp
        print "\nposterior_probabilities:"
        for tag in self.__posterior_probabilities:
            strp = "P(Y=" + str(tag) + ")"
            for dimension, value in enumerate(self.test_x):
                strp = strp + "P(X(" + str(dimension) + ")=" + \
                    str(value) + "|Y=" + str(tag) + ")"
            strp = strp + "=" + str(self.__posterior_probabilities[tag])
            print strp
        print ""

    def get_result(self):
        return self.__result


if __name__ == "__main__":
    xx = [[1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3],
          ['S', 'M', 'M', 'S', 'S', 'S', 'M', 'M', 'L', 'L', 'L', 'M', 'M', 'L', 'L']]
    yy = [-1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1]
    test = [2, 'S']
    bayess = Bayes(xx, yy, test, show=True)
    print bayess.get_result()
    n = 200
    dimensions = 5
    x = np.random.randint(0, 4, size=(dimensions, n))
    y = np.random.randint(0, 3, size=(1, n))
    x_test = np.random.randint(0, 4, size=(1, dimensions))
    bayes = Bayes(x, y[0], x_test[0], show=True)
    print x
    print y
    print x_test
    print bayes.get_result()
