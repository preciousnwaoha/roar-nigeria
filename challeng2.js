


const checkMatch = (string) => {
    reg1 = /[({[<]/
    reg2 = /[)}]>]/
    opens = 0;
    closes = 0;
    for (l in string) {
        console.log(l)
        if (reg1.test(l)) {
            console.log(l.match(reg1))
            opens += 1;
        }
        if (reg1.test(l)) {
            console.log(l.match(reg2))
            closes += 1;
        }
    }
    
    if (opens === closes) {
        console.loh(closes)
        console.log("Match")
    }
    else {
        console.log("Does not match")
    }
}

string_ = "go(to school{} next week()_[or today])"

checkMatch(string_)