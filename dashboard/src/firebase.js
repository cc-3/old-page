import firebase from 'firebase/app';
import 'firebase/auth'
import 'firebase/database';


// app configuration
const config = {
  apiKey: "AIzaSyAjppGwDnI4fjPvwzQHY9jJp044sBU_sCE",
  authDomain: "test-autograders.firebaseapp.com",
  databaseURL: "https://test-autograders.firebaseio.com",
  projectId: "test-autograders",
  storageBucket: "",
  messagingSenderId: "477763975259"
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
  auth.signInWithRedirect(provider).then(() => {
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
