# download-yt

## 当ツールについて

Youtubeから、指定したURLの動画をダウンロードします。
ファイル形式は、動画、音声のみのいずれかから選択可能です。

※音声への変換には、別途`ffmpeg`が必要です。
`ffmpeg`に環境変数を通してください。

## 利用方法

ダウンロードしたいコンテンツのURLを、`download_from_list.py`または`download_from_list.exe`と同階層にある`urls.txt`に改行区切りで列挙してください。

その後、`download_from_list.py`または`download_from_list.exe`を実行してください。
ダウンロードしたいファイルの種類に応じて、第一引数の値を設定してください。

- 動画をダウンロードする場合 → 引数は`video`
例) download_from_list.exe video
`getVideo.bat`に同コマンドが記述されています。
ダウンロードされたファイルは、`videos`フォルダに保存されます。

- 音声をダウンロードする場合 → 引数は`audio`
例) download_from_list.exe audio
`getAudio.bat`に同コマンドが記述されています。
ダウンロードされたファイルは、`audios`フォルダに保存されます。

## 開発環境構築

パッケージ管理ツールには`uv`を利用しています。
事前に`uv`をインストールしてください。
(インストール方法はここでは割愛)

下記コマンドで開発環境が構築されます。

```bash
uv sync --frozen
```

## 実行ファイル(.exe)化

`auto-py-to-exe`を利用して実行ファイル化します。
下記コマンドを実行し、`auto-py-to-exe`を起動してexe化してください。

```bash
uv run auto-py-to-exe
```
