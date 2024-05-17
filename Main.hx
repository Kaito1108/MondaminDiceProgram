import Math;

class Main {
	static public function main() {
		var dice = ["モ", "ン", "ダ", "ミ", "ン", "ン"];
		var diceroll = new Array();
		var count = 0;
		var result = false;

		while (result == false) {
			for (i in 0...6) {
				diceroll.push(dice[Math.floor(Math.random() * 6)]);

				if (diceroll[i] == dice[i] && i == 5) {
					result = true;
				} else if (diceroll[i] == dice[i]) {
					trace(diceroll);
					continue;
				} else {
					count++;
					diceroll = [];
					break;
				}
			}
		}

		trace("Match");
		trace(diceroll);
	}
}
