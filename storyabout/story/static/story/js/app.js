// 3D Scroll

let zSpacing = -2000,
		lastPos = zSpacing / 10,
		$frames = document.getElementsByClassName('frame'),
		frames = Array.from($frames),
		zVals = []

window.onscroll = function() {

	let top = document.documentElement.scrollTop,
			delta = lastPos - top

	lastPos = top

	frames.forEach(function(n, i) {
		zVals.push((i * zSpacing) + zSpacing)
		zVals[i] += delta * -10.5
		let frame = frames[i],
				transform = `translateZ(${zVals[i]}px)`,
				opacity = zVals[i] < Math.abs(zSpacing) / 2 ? 1 : 0
		frame.setAttribute('style', `transform: ${transform}; opacity: ${opacity}`)
	})

}

window.scrollTo(0, 1)

function toggleFrameTypeVisibility(element){
	const paragraphDiv = document.getElementById('frame__paragraph');
	const imageDiv = document.getElementById('frame__image');

	if(element.id === 'paragraph'){
		paragraphDiv.classList.remove('d-none');
		imageDiv.classList.add('d-none');
	}else{
		imageDiv.classList.remove('d-none');
		paragraphDiv.classList.add('d-none');
	}
}
