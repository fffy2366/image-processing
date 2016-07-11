var crypto = require('crypto');
var data = "test";
console.log('Original cleartext: ' + data);
//var algorithm = 'aes-128-ecb';
var algorithm = 'aes-128-cbc';
var key = '7854156156611111';
var clearEncoding = 'utf8';
//var iv = "";
var iv = "0000000000000000";
//If the next line is uncommented, the final cleartext is wrong.
var cipherEncoding = 'base64';

/*var cipher = crypto.createCipheriv(algorithm, key, iv);
cipher.setAutoPadding(true);
var cipherChunks = [];
cipherChunks.push(cipher.update(data, clearEncoding, cipherEncoding));
cipherChunks.push(cipher.final(cipherEncoding));
console.log(cipherEncoding + ' ciphertext: ' + cipherChunks.join(''));



var decipher = crypto.createDecipheriv(algorithm, key, iv);
var plainChunks = [];
for (var i = 0; i < cipherChunks.length; i++) {
    plainChunks.push(decipher.update(cipherChunks[i], cipherEncoding, clearEncoding));
}
plainChunks.push(decipher.final(clearEncoding));
console.log("UTF8 plaintext deciphered: " + plainChunks.join(''));*/


//data 是准备加密的字符串,key是你的密钥
function encryption(data, key) {
    var iv = "0000000000000000";
    var clearEncoding = 'utf8';
    var cipherEncoding = 'base64';
    var cipherChunks = [];
    var cipher = crypto.createCipheriv('aes-128-cbc', key, iv);
    cipher.setAutoPadding(true);

    cipherChunks.push(cipher.update(data, clearEncoding, cipherEncoding));
    cipherChunks.push(cipher.final(cipherEncoding));

    return cipherChunks.join('');
}
//data 是你的准备解密的字符串,key是你的密钥
function decryption(data, key) {
    var iv = "0000000000000000";
    var clearEncoding = 'utf8';
    var cipherEncoding = 'base64';
    var cipherChunks = [];
    var decipher = crypto.createDecipheriv('aes-128-cbc', key, iv);
    decipher.setAutoPadding(true);

    cipherChunks.push(decipher.update(data, cipherEncoding, clearEncoding));
    cipherChunks.push(decipher.final(clearEncoding));

    return cipherChunks.join('');
}

console.log(encryption(data, key)) ;
