from downey_code.thinkbayes import Pmf


class Cookie(Pmf):
    """クッキーボウルのid(string)を確率に対応させるmap"""

    def __init__(self, hypos):
        """Initialize self.data

        hypos: クッキーボウルのid(string)
        """
        Pmf.__init__(self)
        for hypo in hypos:
            self.Set(hypo, 1)
        self.Normalize()

    def Update(self, data):
        """PMFを新しいデータでアップデート

        data: クッキーの種類(string)
        """
        for hypo in self.Values():
            like = self.Likelihood(data, hypo)
            self.Mult(hypo, like)
        self.Normalize()

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

    pmf = Cookie(hypos)

    pmf.Update('vanilla')

    for hypo, prob in pmf.Items():
        print(hypo, prob)


if __name__ == '__main__':
    main()
