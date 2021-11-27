gsap.registerPlugin(ScrollTrigger);

gsap.to('.firt_message_animation',{
    ScrollTrigger:{
        trigger: '.firt_message_animation',
        toggleAction: 'restart pause reverse pause'
    },
    duration: 4,
    x: 300,
});