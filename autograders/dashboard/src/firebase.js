import firebase from 'firebase/app';
import 'firebase/auth'
import 'firebase/database';


// app configuration
const config = {
  apiKey: "AIzaSyDEVdqQMsO2ulwiw93wUGOYUtzEfFAZncs",
  authDomain: "autograders-cc3.firebaseapp.com",
  databaseURL: "https://autograders-cc3.firebaseio.com",
  projectId: "autograders-cc3",
  storageBucket: "autograders-cc3.appspot.com",
  messagingSenderId: "1077556258829"
};

// app initialization
firebase.initializeApp(config);

// google auth provider
const provider = new firebase.auth.GoogleAuthProvider();

// firebase authentication
const auth = firebase.auth();

// firebase database
const database = firebase.database();

// sign in
const signIn = () => {
  auth.signInWithPopup(provider).then(() => {
    window.M.toast({html: 'Logged In'});
  }).catch((err) => {
    window.M.toast({html: err});
  });
};

// sign out
const signOut = () => {
  auth.signOut().then(() => {
    window.M.toast({html: 'Sign Out'});
  }).catch((err) => {
    window.M.toast({html: err});
  });
};


export { database, provider, auth, signIn, signOut };
