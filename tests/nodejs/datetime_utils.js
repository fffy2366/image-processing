var moment = require('moment');
console.log(moment().format("YYYY-MM-DD HH:mm:ss")) ;
console.log(moment(1468237060*1000).format("YYYY-MM-DD HH:mm:ss")) ;

console.log(moment().second()) ;
console.log(parseInt((moment().unix()-1468237060)/60)>5) ;