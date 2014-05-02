
#include <iostream>
#include <vector>

using namespace std;

enum Type { STRAIGHT, CURVE };
enum Direction { N, NE, E, SE, S, SW, W, NW };
const int NUM_STRAIGHT = 4;
const int NUM_CURVE = 12;

struct Piece {
	Type type;
	bool reversable;
	unsigned xinc;
	unsigned yinc;
};

struct Solution {
	vector<Piece> pieces;
	int x;
	int y;
	Direction direction;
};

vector<Piece> pieces;
vector<Solution> solutions;

void init() {
	for (int i=0; i < NUM_STRAIGHT; i++) {
		Piece piece;
		piece.type = STRAIGHT;
		piece.xinc = 2;
		piece.yinc = 2;
		piece.reversable = false;	
		pieces.push_back(piece);
	}	
	for (int i=0; i < NUM_CURVE; i++) {
		Piece piece;
		piece.type = CURVE;	
		piece.xinc = 1;
		piece.yinc = 1;
		piece.reversable = true;	
		pieces.push_back(piece);
	}
}

void solveit(Solution solution, vector<Piece> pieces) {

	for (auto piece : pieces) {
		cout << "piece, type: " << piece.type << endl;
		if (piece.type == CURVE) {
			switch (solution.direction) {
				case N: solution.x += piece.xinc; solution.y += piece.yinc; break;
				case NE: solution.x += piece.xinc; solution.y += piece.yinc; break;
				case E: solution.x += piece.xinc; solution.y += piece.yinc; break;
				case SE: solution.x += piece.xinc; solution.y += piece.yinc; break;
				case S: solution.x += piece.xinc; solution.y += piece.yinc; break;
				case SW: solution.x += piece.xinc; solution.y += piece.yinc; break;
				case W: solution.x += piece.xinc; solution.y += piece.yinc; break;
				case NW: solution.x += piece.xinc; solution.y += piece.yinc; break;
			}
		}
		else if (piece.type == STRAIGHT) {
			switch (solution.direction) {
				case N: break; 
				case NE: break;
				case E: break;
				case SE: break;
				case S: break;
				case SW: break;
				case W: break;
				case NW: break;
			}
		}
	}
}


int main() {
	cout << "main, begin" << endl;
	init();
	//solveit();
	cout << "piece count: " << pieces.size() << endl;
}
