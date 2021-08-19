# プログラミング向けフォント Firsh

Firsh は、[Fira Code](https://github.com/tonsky/FiraCode) と [源ノ角ゴシック](https://github.com/adobe-fonts/source-han-sans) を合成したプログラミング向けフォントです。

プログラミング向けフォント [Firple](https://github.com/negset/Firple/) の姉妹フォントです。

![Firsh Regular サンプル](https://github.com/negset/Firsh/raw/images/sample.png)

## 特徴

- 豊富で美麗なグリフ

  Fira Code が持つグリフを全てそのまま利用できます。  
  それ以外のグリフは源ノ角ゴシック由来のものが適用されます。

- 横幅を 1:2 に調整

  半角文字と全角文字の横幅の比を 1:2 に揃えています。

- リガチャに対応

  Fira Code が持つプログラミング向けのリガチャを利用できます。

- 2 種のウェイト

  Regular と Bold の 2 ウェイトがあります。

## フォントファミリー

フォント名   |説明
:------------|:----------------------------------------
Firsh Regular|Fira Code Regular + Source Han Sans Regular
Firsh Bold   |Fira Code Bold + Source Han Sans Bold

## ライセンス

[SIL Open Font License (OFL) Version 1.1](https://github.com/negset/Firsh/blob/master/LICENSE.txt)

## ダウンロード

[Releases ページ](https://github.com/negset/Firsh/releases) から入手できます。

## ビルド

### 必要なもの

- FontForge および fontTools

```
$ sudo apt install fontforge
$ sudo apt install fonttools
```

- 元となるフォントファイル

```
fonts/FiraCode-Bold.ttf
fonts/FiraCode-Regular.ttf
fonts/SourceHanSans-Bold.ttf
fonts/SourceHanSans-Regular.ttf
```

### コマンド

```
$ ./build.sh
```