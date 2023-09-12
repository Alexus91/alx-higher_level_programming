#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let inx = 0; inx < x; inx++) {
    theFunction();
  }
};
