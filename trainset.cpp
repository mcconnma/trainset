
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

enum Type { STRAIGHT, CURVE };
enum Direction { N, NE, E, SE, S, SW, W, NW };

const int RADIUS = 4;
const double incx = 2.83;

struct Piece {
	Type type;
	bool reversable;
	unsigned xinc;
	unsigned yinc;
};

class Solution {
public:
	Solution();
	void add(Piece piece) { pieces.push_back(piece); }
	int x;
	int y;
	Direction direction;
private:
	vector<Piece> pieces;
};

Solution::Solution() : x(0), y(0), direction(N) {
}

class TrainSet {
public:
	const int NUM_STRAIGHT = 0;
	const int NUM_CURVE = 8;
	TrainSet();
	void solve();
	void recurse(Solution solution, vector<Piece> pieces);
private:
	vector<Piece> pieces;
	vector<Solution> solutions;
};

TrainSet::TrainSet() {
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
	cout << "piece count: " << pieces.size() << endl;
}

void TrainSet::recurse(Solution solution, vector<Piece> pieces) {

	for (auto piece : pieces) {
		pieces.pop_back();
		if (piece.type == CURVE) {
			switch (solution.direction) {
				case N: solution.x += piece.xinc; solution.y += piece.yinc; solution.direction = NE; break;
				case NE: solution.x += piece.xinc; solution.y += piece.yinc; solution.direction = E; break;
				case E: solution.x += piece.xinc; solution.y -= piece.yinc; solution.direction = SE; break;
				case SE: solution.x += piece.xinc; solution.y -= piece.yinc; solution.direction = S; break;
				case S: solution.x -= piece.xinc; solution.y -= piece.yinc; solution.direction = SW; break;
				case SW: solution.x -= piece.xinc; solution.y -= piece.yinc; solution.direction = W; break;
				case W: solution.x -= piece.xinc; solution.y += piece.yinc; solution.direction = NW; break;
				case NW: solution.x -= piece.xinc; solution.y += piece.yinc; solution.direction = N; break;
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
		recurse(solution, pieces);
		cout << "solution: x = " << solution.x << ", y = " << solution.y << endl;
	}
}

void TrainSet::solve() {

	//for (auto piece : pieces) {
	for (auto i = pieces.rbegin(); i != pieces.rend(); ++i) {
		cout << "piece, type: " << (*i).type << endl;
		Solution solution;
		//solution.add(*i);
		//pieces.pop_back();
		recurse(solution, pieces);
	}
}


int main() {
	cout << "main, begin" << endl;
	TrainSet trainset;
	trainset.solve();
}
