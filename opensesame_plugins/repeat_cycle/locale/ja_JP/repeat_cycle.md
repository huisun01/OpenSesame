# Repeat_cycle: リピートサイクル

このプラグインを使用すると、`loop` の一連の動作(サイクル)を繰り返すことができます。 一般的には、参加者がミスをしたときや応答時間が遅すぎるときに試行を繰り返すために使用されます。

例えば、応答時間が 3000 ms を超過するすべての試行を繰り返すためには、`repeat_cycle (リピートサイクル)`アイテムを(一般的には) `keyboard_response (キーボード応答)`アイテムの後に設置し、以下の実行条件を設定します:

	[response_time] > 3000

また、以下のように`inline_script (インラインスクリプト)`で変数を1とすることで、強制的にサイクルを繰り返すことができます:

	var.repeat_cycle = 1
