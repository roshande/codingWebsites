var _requirejs = requirejs; requirejs = undefined; var _require = require; require = undefined; var _define = define; define = undefined;
// CodeMirror, copyright (c) by Marijn Haverbeke and others
!function(mod){"object"==typeof exports&&"object"==typeof module?mod(require("../../lib/codemirror")):"function"==typeof define&&define.amd?define(["../../lib/codemirror"],mod):mod(CodeMirror)}(function(CodeMirror){"use strict";CodeMirror.defineMode("shell",function(){function define(style,string){for(var split=string.split(" "),i=0;i<split.length;i++)words[split[i]]=style}function tokenBase(stream,state){if(stream.eatSpace())return null;var sol=stream.sol(),ch=stream.next();if("\\"===ch)return stream.next(),null;if("'"===ch||'"'===ch||"`"===ch)return state.tokens.unshift(tokenString(ch,"`"===ch?"quote":"string")),tokenize(stream,state);if("#"===ch)return sol&&stream.eat("!")?(stream.skipToEnd(),"meta"):(stream.skipToEnd(),"comment");if("$"===ch)return state.tokens.unshift(tokenDollar),tokenize(stream,state);if("+"===ch||"="===ch)return"operator";if("-"===ch)return stream.eat("-"),stream.eatWhile(/\w/),"attribute";if(/\d/.test(ch)&&(stream.eatWhile(/\d/),stream.eol()||!/\w/.test(stream.peek())))return"number";stream.eatWhile(/[\w-]/);var cur=stream.current();return"="===stream.peek()&&/\w+/.test(cur)?"def":words.hasOwnProperty(cur)?words[cur]:null}function tokenString(quote,style){var close="("==quote?")":"{"==quote?"}":quote;return function(stream,state){for(var next,end=!1,escaped=!1;null!=(next=stream.next());){if(next===close&&!escaped){end=!0;break}if("$"===next&&!escaped&&"'"!==quote){escaped=!0,stream.backUp(1),state.tokens.unshift(tokenDollar);break}if(!escaped&&next===quote&&quote!==close)return state.tokens.unshift(tokenString(quote,style)),tokenize(stream,state);escaped=!escaped&&"\\"===next}return(end||!escaped)&&state.tokens.shift(),style}}function tokenize(stream,state){return(state.tokens[0]||tokenBase)(stream,state)}var words={};define("atom","true false"),define("keyword","if then do else elif while until for in esac fi fin fil done exit set unset export function"),define("builtin","ab awk bash beep cat cc cd chown chmod chroot clear cp curl cut diff echo find gawk gcc get git grep kill killall ln ls make mkdir openssl mv nc node npm ping ps restart rm rmdir sed service sh shopt shred source sort sleep ssh start stop su sudo tee telnet top touch vi vim wall wc wget who write yes zsh");var tokenDollar=function(stream,state){state.tokens.length>1&&stream.eat("$");var ch=stream.next();return/['"({]/.test(ch)?(state.tokens[0]=tokenString(ch,"("==ch?"quote":"{"==ch?"def":"string"),tokenize(stream,state)):(/\d/.test(ch)||stream.eatWhile(/\w/),state.tokens.shift(),"def")};return{startState:function(){return{tokens:[]}},token:function(stream,state){return tokenize(stream,state)},closeBrackets:"()[]{}''\"\"``",lineComment:"#",fold:"brace"}}),CodeMirror.defineMIME("text/x-sh","shell")});
var requirejs = _requirejs; _requirejs = undefined; var require = _require; _require = undefined; var define = _define; _define = undefined;