Meteor.methods({
	toggleAdmin(id){
		if(Roles.userIsInRole(id, 'admin')){
			Roles.removeUsersFromRoles(id, 'admin');
		}
		else{
			Roles.addUsersToRoles(id, 'admin');
		}
	},
	toggleReset(id){
		Accounts.sendResetPasswordEmail(id);
	},
	addWallet: function( wallet ) {
    check( wallet, Wallet.simpleSchema() );
  }
});
