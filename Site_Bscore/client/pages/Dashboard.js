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
