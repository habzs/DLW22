const rootRef = db.ref('vacant');

// function addData() {
//     writeUserData();
//     console.log("ua");

// }

function addData() {
    console.log("Changed");
    // rootRef.child("one").set({
    //     state: "true"
    // });

    var nowie = moment().format();

    const newData = {
        state: "false",
        time: nowie,
    };

    const updates = {};
    updates['/vacant/' + "one"] = newData;
    db.ref().update(updates);

}


// db.ref("/vacant/one")
rootRef.on('value', (snapshot) => {
    const data = snapshot.val();
    console.log("data: ", data.one.state);
    changeColor(data.one.state)
})





// function removeAll() {
//     var list = document.getElementById("cafe-list");
//     while (list.hasChildNodes()) {
//         list.removeChild(list.firstChild);
//     }

// }


// function addData() {

//     randomNum = Math.random();

//     console.log("addClick");

//     db.collection("cafes").add({
//         name: `Nama: ${randomNum}`,
//         city: `Citee: ${randomNum}`,
//     })
//         .then(() => {
//             console.log("Document successfully written!");
//         })
//         .catch((error) => {
//             console.error("Error writing document: ", error);
//         });
// }





// const cafeList = document.querySelector('#cafe-list');
// const form = document.querySelector('#add-cafe-form');

// // create element & render cafe
// function renderCafe(doc) {
//     let li = document.createElement('li');
//     let name = document.createElement('span');
//     let city = document.createElement('span');
//     let cross = document.createElement('div');

//     li.setAttribute('data-id', doc.id);
//     name.textContent = doc.data().name;
//     city.textContent = doc.data().city;
//     cross.textContent = 'x';

//     li.appendChild(name);
//     li.appendChild(city);
//     li.appendChild(cross);

//     cafeList.appendChild(li);

//     // deleting data
//     cross.addEventListener('click', (e) => {
//         e.stopPropagation();
//         let id = e.target.parentElement.getAttribute('data-id');
//         db.collection('cafes').doc(id).delete();
//     });
// }

// // getting data
// // db.collection('cafes').orderBy('city').get().then(snapshot => {
// //     snapshot.docs.forEach(doc => {
// //         renderCafe(doc);
// //     });
// // });

// // saving data
// form.addEventListener('submit', (e) => {
//     e.preventDefault();
//     db.collection('cafes').add({
//         name: form.name.value,
//         city: form.city.value
//     });
//     form.name.value = '';
//     form.city.value = '';
// });

// // real-time listener
// db.collection('cafes').orderBy('city').onSnapshot(snapshot => {
//     let changes = snapshot.docChanges();
//     changes.forEach(change => {
//         console.log(change.doc.data());
//         if (change.type == 'added') {
//             renderCafe(change.doc);
//         } else if (change.type == 'removed') {
//             let li = cafeList.querySelector('[data-id=' + change.doc.id + ']');
//             cafeList.removeChild(li);
//         }

//         // currentState = change.doc.state;
//         if (change.type == 'modified') {
//             console.log("whatChanged: ", change.doc);
//             changeColor(change.doc);
//         }

//     });
// });


function changeColor(state) {
    if (state === "true") {
        document.getElementById("testor").setAttribute("style", "background-color: green; height: 500px");
    } else {
        document.getElementById("testor").setAttribute("style", "background-color: red; height: 500px");
    }
}



// function writeUserData(userId, name, email, imageUrl) {
//     firebase.database().ref('users/' + userId).set({
//         username: name,
//         email: email,
//         profile_picture: imageUrl
//     });
// }
