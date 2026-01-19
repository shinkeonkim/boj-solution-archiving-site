use std::io;

fn main() {
    let mut s = String::new();
    io::stdin().read_line(&mut s);
    
    let ret = s.trim()
        .split_whitespace()
        .map(|x| x.parse::<i32>().unwrap())
        .sum::<i32>();
    
    println!("{}", ret);
}