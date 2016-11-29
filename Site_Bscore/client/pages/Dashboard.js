//Returns boolean status of whether the current users is an admin
Meteor.subscribe('wallet', function () {
	$.get('https://api.blockcypher.com/v1/btc/main/addrs/1DEP8i3QJCsomS4BSMY2RpU1upv62aGvhD/balance')
  .then(function(d) {Wallet.insert(d)} );
});

Template.Dashboard.helpers({
	admin: function(){
		return Roles.userIsInRole(Meteor.userId(), 'admin');
	},
	wallet (){
		return Wallet.findOne();
	}
});

Template.card.helpers({
	wallet (){
		return Wallet.findOne();
	},
	objlist (){
		var result = [];
		var obj = Wallet.findOne();
		for (var key in obj){
			if(key != 'address' && key != "unconfirmed_balance" && key != "n_tx"
			&& key !="unconfirmed_n_tx" && key != "final_n_tx" && key != "_id"){
				result.push({name:key,value:obj[key]});
			}
		}
    return result;
	}
});
