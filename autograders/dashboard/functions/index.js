'use strict';

const functions = require('firebase-functions');
const admin = require('firebase-admin');
admin.initializeApp();


// Keeps track of the length of the 'likes' child list in a separate property.
exports.queuesize = functions.database.ref('/queue').onWrite(
  async (change) => {
    const collectionRef = change.after.ref.parent;
    const countRef = collectionRef.child('queue_size');

    let increment;
    if (change.after.exists() && !change.before.exists()) {
      increment = 1;
    } else if (!change.after.exists() && change.before.exists()) {
      increment = -1;
    } else {
      return null;
    }

    // Return the promise from countRef.transaction() so our function
    // waits for this async event to complete before it exits.
    await countRef.transaction((current) => {
      return Math.max((current || 0) + increment, 0);
    });
    console.log('Counter updated.');
    return null;
  });


// If the number of enqueue files gets deleted, recount the number of likes
exports.recomputesize = functions.database.ref('/queue_size').onDelete(async (snap) => {
  const counterRef = snap.ref;
  const collectionRef = counterRef.parent.child('/queue_size');

  // Return the promise from counterRef.set() so our function
  // waits for this async event to complete before it exits.
  const messagesData = await collectionRef.once('value');
  return await counterRef.set(messagesData.numChildren());
});
