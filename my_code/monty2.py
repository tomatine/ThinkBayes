from downey_code.thinkbayes import Suite


class Monty(Suite):
    def Likelihood(self, data, hypo):
        """仮説のもとでの尤度を計算

        hypo: string 商品のあるドア
        data: string モンティの開けたドア
        """
        if hypo == data:
            return 0
        elif hypo == 'A':
            return 0.5
        else:
            return 1


def main():
    hypos = 'ABC'
    suite = Monty(hypos)

    data = 'B'
    suite.Update(data)

    suite.Print()


if __name__ == '__main__':
    main()
