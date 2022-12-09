package main

import "fmt"

func main() {
	// var myMap = map[int]string{}
	// fmt.Print(myMap)

	// myMap := map[string]int{}
	// fmt.Print(myMap)

	// var myMap = map[int]string{1: "Nandu", 2: "Gopal", 3: "Devaraj"}
	// fmt.Print(myMap)

	// myMap := map[string]int{"English": 20, "Maths": 30, "Science": 40}
	// fmt.Print(myMap)

	// Creating empty map

	// var a = make(map[string]string) // false
	// var a = map[string]string{} // false
	// var b map[int]string        // true

	// fmt.Println(a == nil)
	// fmt.Println(b == nil)

	// Accessing elements in maps

	// var a = map[string]string{"brand": "Ford", "model": "Mustang", "year": "1964"}

	// fmt.Println(a["brand"])
	// fmt.Println(a["model"])
	// fmt.Println(a["year"])

	// Deleting the elements

	// var a = map[string]string{"brand": "Ford", "model": "Mustang", "year": "1964"}

	// delete(a, "year")
	// fmt.Println(a)
	// delete(a, "model")
	// fmt.Println(a)

	// Updating a element

	// var a = map[string]string{"brand": "Ford", "model": "Mustang", "year": "1964"}
	// fmt.Println(a)

	// a["year"] = "1970"
	// fmt.Println(a)

	// Adding a element to the map

	// var a = make(map[string]string)
	// a["brand"] = "Ford"
	// a["model"] = "Mustang"
	// a["year"] = "1964"

	// fmt.Println(a)

	// a["color"] = "red"
	// a["budget"] = "300,000,000"

	// fmt.Println(a)

	// Check for the specific element in the map
	// check gives the true or flase values

	// var a = map[string]string{"brand": "Ford", "model": "Mustang", "year": "1964", "day": ""}

	// val1, check1 := a["brand"] // existing key and value
	// val2, check2 := a["color"] // non-existing key and value
	// val3, check3 := a["day"]   // existing key but empty value(empty string)
	// _, check4 := a["model"]    // only checking for the value not for the key

	// fmt.Println(val1, check1)
	// fmt.Println(val2, check2)
	// fmt.Println(val3, check3)
	// fmt.Println(check4)

	// Maps are the references
	// Changing the elements in the duplicate map will also change the original map elements also
	// var a = map[string]string{"brand": "Ford", "model": "Mustang", "year": "1964"}
	// b := a

	// fmt.Println(a)
	// fmt.Println(b)

	// b["year"] = "2000"
	// fmt.Println("copying and changing the element :: ")

	// fmt.Println(a)
	// fmt.Println(b)

	// Iterating over maps

	// var a = map[string]string{"brand": "Ford", "model": "Mustang", "year": "1964"}

	// for k, v := range a {
	// 	fmt.Println(k, v)
	// }

	// var a = map[string]string{"brand": "Ford", "model": "Mustang", "year": "1964"}

	// for _, v := range a {
	// 	fmt.Println(v)
	// }

	var a = map[string]string{"brand": "Ford", "model": "Mustang", "year": "1964"}

	for k, _ := range a {
		fmt.Println(k)
	}

}
