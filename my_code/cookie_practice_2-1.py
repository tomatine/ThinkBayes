from downey_code.thinkbayes import Suite


class Cookie(Suite):
    """クッキーボウルのid(string)を確率に対応させるmap"""

    mixes = {
        'Bowl 1': dict(vanilla=0.75, chocolate=0.25),
        'Bowl 2': dict(vanilla=0.5, chocolate=0.5)
    }

    def Likelihood(self, data, hypo):
        """仮説(hypo)のもとでのデータの尤度

        data: クッキーの種類(string)
        hypo: クッキーボウルのid(string)
        """
        mix = self.mixes[hypo]
        like = mix[data]
        return like


def main():
    hypos = ['Bowl 1', 'Bowl 2']

    suite = Cookie(hypos)

    suite.Update('vanilla')
    suite.Update('chocolate')
    suite.Update('chocolate')

    for hypo, prob in suite.Items():
        print(hypo, prob)


if __name__ == '__main__':
    main()
