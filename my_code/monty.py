from downey_code.thinkbayes import Pmf

class Monty(Pmf):
    """車の位置を確率に対応付ける"""
    def __init__(self,hypos):
        """確率分布を初期化

        hypos: 仮説
        """
        Pmf.__init__(self)
        for hypo in hypos:
            self.Set(hypo,1)
        self.Normalize()

    def Update(self,data):
        """データに基づいて仮説を更新

        data: データの任意の表現
        """
        for hypo in self.Values():
            like=self.Likelihood(data,hypo)
            self.Mult(hypo,like)
        self.Normalize()

    def Likelihood(self,data,hypo):
        """仮説の下での尤度を計算

        hypo: string 商品がある扉の名前
        data: string モンティが開けた扉の名前
        """
        if hypo==data:
            return 0
        elif hypo=='A':
            return 0.5
        else:
            return 1


def main():
    hypos='ABC'
    pmf=Monty(hypos)

    data='B'
    pmf.Update(data)

    for hypo,prob in sorted(pmf.Items()):
        print(hypo,prob)


if __name__ == '__main__':
    main()
