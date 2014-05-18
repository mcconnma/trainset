function string_recurse(active, rest) {
    if (rest.length == 0) {
        console.log(active);
    } else {
        string_recurse(active + rest.charAt(0), rest.substring(1, rest.length));
        string_recurse(active, rest.substring(1, rest.length));
    }
}
string_recurse("", "111112222");
