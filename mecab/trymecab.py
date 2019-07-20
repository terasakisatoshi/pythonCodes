# -*- coding: utf-8 -*-
from natto import MeCab


def main():
    nm = MeCab('-Owakati')
    word = "MeCabは 京都大学情報学研究科−日本電信電話株式会社コミュニケーション科学基礎研究所 共同研究ユニットプロジェクトを通じて開発されたオープンソース 形態素解析エンジンです。 言語, 辞書,コーパスに依存しない汎用的な設計を 基本方針としています。 パラメータの推定に Conditional Random Fields (CRF) を用 いており, ChaSenが採用している 隠れマルコフモデルに比べ性能が向上しています。また、平均的に ChaSen, Juman, KAKASIより高速に動作します。 ちなみに和布蕪(めかぶ)は, 作者の好物です。"
    print(nm.parse(word))
    lis = [n.surface for n in nm.parse(word, as_nodes=True) if n.is_nor()]
    print(lis)
if __name__ == '__main__':
    main()
