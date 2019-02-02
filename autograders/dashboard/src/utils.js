import moment from 'moment';
import queryString from 'query-string';

import { history } from './router';
import { database } from './firebase';


export const getRandomEmoji = () => {
  const emojis = [
    '\\(o_o)/',
    '\\(^Д^)/',
    '(;-;)',
    '(≥o≤)',
    '(>_<)',
    '(·.·)',
    '(=\'X\'=)',
    '(^_^)b',
    '(o^^)o',
    '(˚Δ˚)b',
    '(·_·)',
    '(^-^*)'
  ];
  return emojis[Math.floor(Math.random() * emojis.length)];
};

export const getDate = (utc, format=false) => {
  const date = moment(moment.utc(utc, 'YYYY-MM-DDTHH:mm:ss').toDate()).local();
  if (!format)
    return date.toDate();
  return date.format('YYYY/MM/DD, HH:mm:ss');
};

export const getSearch = () => {
  const q = history.location.search
  return queryString.parse(q).s ? queryString.parse(q).s : '';
};

export const attach = (path, callback) => {
  return database.ref(path).on('value', snap => callback(snap.val()));
};

export const dettach = (path, callback) => {
  return database.ref(path).on('value', snap => callback(snap.val()));
}
