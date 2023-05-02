#!/usr/bin/node

class Rectangle {
	  constructor (w, h) {
		      if (w <= 0 || h <= 0 || typeof w !== 'number' || typeof h !== 'number') {
			            return 'Rectangle {}';
			          }

		      this.width = w;
		      this.height = h;
		    }

	  print () {
		      for (let i = 0; i < this.height; i++) {
			            console.log('X'.repeat(this.width));
			          }
		    }
}

module.exports = Rectangle;
