Wallet = new Meteor.Collection('wallet');
Wallet.allow({
  insert() {
    if ( Meteor.user() ) {
          return true;
        }
    else {
          return false;
        }
    },
  update() { return false; },
  remove() { return false; }
});

WalletSchema = new SimpleSchema({
  // Schema rules
  "address": {
    type: String,
    label: "Wallet Address"
  },
  "total_received": {
    type: Number,
    label: "Total Recieved"
  },
  "balance": {
    type: Number,
    label: "Balance"
  },
  "unconfirmed_balance": {
    type: Number,
    label: "Unconfirmed Balance"
  },
  "final_balance": {
    type: Number,
    label: "Final Balance"
  },
  "n_tx": {
    type: Number,
    label: "N TX"
  },
  "unconfirmed_n_tx": {
    type: Number,
    label: "Unconfirmed N TX"
  },
  "final_n_tx": {
    type: Number,
    label: "Final N TX"
  }
});

Wallet.attachSchema( WalletSchema );
