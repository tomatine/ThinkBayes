from downey_code.thinkbayes import Suite

class M_and_M(Suite):
    """仮説（AまたはB）から確率への対応付け"""
    mix94=dict(brown=30,
               yellow=20,
               red=20,
               green=10,
               orange=10,
               tan=10,
               blue=0
               )

    mix96=dict(blue=24,
               green=20,
               orange=20,
               yellow=14,
               red=13,
               brown=13,
               tan=0
               )

    hypoA=dict(bag1=mix94,bag2=mix96)
    hypoB=dict(bag1=mix96,bag2=mix94)

    hypotheses=dict(A=hypoA,B=hypoB)

    def Likelihood(self, data, hypo):
        """仮説の下での尤度を計算

        hypo: string 仮説（AまたはB）
        data: tuple of string bag, string color
        """
        bag,color=data
        mix=self.hypotheses[hypo][bag]
        like=mix[color]
        return like


def main():
    suite=M_and_M('AB')

    suite.Update(('bag1','green'))
    suite.Update(('bag2','brown'))

    suite.Print()


if __name__ == '__main__':
    main()