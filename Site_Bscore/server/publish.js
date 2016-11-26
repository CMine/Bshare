Meteor.publish('allUsers', function(){
	if(Roles.userIsInRole(this.userId, 'admin')){
		return Meteor.users.find({});
	}
	else{
		this.stop();
		return
	}
});

Meteor.publish('Accounts', function(){
	return Meteor.Accounts.find({});
});

Meteor.publish('wallet', function(){
	return Wallet.find({});
});
