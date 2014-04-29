
#include <iostream>
#include <vector>

using namespace std;

enum Type { STRAIGHT, CURVE };
const int NUM_STRAIGHT = 4;
const int NUM_CURVE = 12;

struct Piece {
	Type type;
};

struct Solution {
	vector<Piece> pieces;
};

vector<Piece> pieces;
vector<Solution> solutions;

void init() {
	for (int i=0; i < NUM_STRAIGHT; i++) {
		Piece piece;
		piece.type = STRAIGHT;	
		pieces.push_back(piece);
	}	
	for (int i=0; i < NUM_CURVE; i++) {
		Piece piece;
		piece.type = CURVE;	
		pieces.push_back(piece);
	}
}


int main() {
	cout << "main, begin" << endl;
	init();
	cout << "piece count: " << pieces.size() << endl;
}
