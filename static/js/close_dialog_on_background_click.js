const modalLightDismiss = ( () => {
const dialogs = document.querySelectorAll('dialog');
for (const dialog of dialogs) {
	dialog.addEventListener('click', (event) => {
		if (event.target === dialog) dialog.close()
	});

	// Stop propagation for clicks inside the dialog
	const dialogContent = dialog.querySelector('h1');
	dialogContent.addEventListener('click', (event) => {
		event.stopPropagation();
	});
}
})();