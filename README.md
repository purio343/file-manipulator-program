# file-manipulator-program

## 概要
様々な命令を受けてその内容を実行するCLIスクリプトです。
現状、4種の命令を受け付けることができます。

## 使い方
以下のようにコマンドを実行します。

```bash
python3 file_manipulator_program.py <instruction> <input_file_path> [additional_args]
```

`<instruction>`には、下記のいずれかを使用してください。
- reverse
- copy
- duplicate-contents
- replace-string

### reverse
入力元のファイルの内容を反転したものを、出力先に作成します。

```bash
python3 file_manipulator_program.py reverse <input_file_path> <output_file_path>
```

- `<input_file_path>`：入力元となるファイルのパス。
- `<output_file_path>`：出力先となるファイルのパス。

### copy
入力元のファイルの内容を、出力先に作成します。

```bash
python3 file_manipulator_program.py copy <input_file_path> <output_file_path>
```

- `<input_file_path>`：入力元となるファイルのパス。
- `<output_file_path>`：出力先となるファイルのパス。

### duplicate-contents
入力元のファイルの内容を、同ファイルにn回複製します。

```bash
python3 file_manipulator_program.py duplicate-contents <input_file_path> <n>
```

- `<input_file_path>`：入力元となるファイルのパス。
- `<n>`：複製を行う回数。

### replace-string
入力元のファイルの内容に存在する任意の文字列を、他の文字列に置き換えます。

```bash
python3 file_manipulator_program.py replace-string <input_file_path> <old_string> <new_string>
```

- `<input_file_path>`：入力元となるファイルのパス。
- `<old_string>`：置き換え元の文字列。
- `<new_string>`：置き換え先の文字列。
