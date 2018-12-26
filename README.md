# FFConverter

## Font Agenda
---
### Responsive Font size 
- Large : For larger displays and all devices with large viewports 
- Medium : For tablet devices and all displays with medium vieports
- Small : For smartphones and all displays with smaller viewports
---
### Ways to implement responsive font size
#### [Media Queries ](https://stackoverflow.com/questions/15649244/responsive-font-size) :

```css
      @media only screen and (max-width: 320px) {
    
       body { 
          font-size: 2em; 
       }
    
    }
```
#### [Using Viewport Sizes ](https://stackoverflow.com/questions/15649244/responsive-font-size) :
```css
    h1 {
      font-size: 5.9vw;
    }
    h2 {
      font-size: 3.0vh;
    }
    p {
      font-size: 2vmin;
    }

```
#### done by saahil
