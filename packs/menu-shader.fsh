uniform vec2 center; 
uniform vec2 resolution;
uniform float time;
uniform vec2 mouse; 
uniform float pulse1;
uniform float pulse2;
uniform float pulse3; 


vec3 c;
void ori(vec2 p,out vec3 c)
{
    float t = time;
    c=vec3(0.3/p.y-0.1,sin(t*0.2)-0.5,0.7);
    if (length(vec2(p.x,p.y-0.45))<0.4 &&
    mod(9.0,0.25/(p.y-0.2))<0.7+abs(cos(t*100.0)*cos(t*33.3))){
        c=vec3(1.0,0.4+(p.y*3.0-1.5),0.0);
    }
    
    float mt=(asin(sin(p.x*50.0))+asin(sin(p.x*15.0))*2.0-asin(sin(p.x*80.0))/10.0)/90.0;
    if (p.y<mt+abs(p.x)/8.0+0.3){
        c=vec3(0.01);
    }

    float w = 2.0 + p.y/10.0;
    vec2 q1 =p*w/(p.y-0.3);
    q1.y = q1.y/0.1 - t+cos(t)*0.2;  
    float size =0.7;
    vec2 q2 = abs(mod(q1, size)-size/2.0);
    float f = (max(q2.x,q2.y)-0.3)*10.0;
    if (p.y<0.2){
    c = vec3(1.0,0.2,1.0)*f;
    }
}

void fil(vec2 p,inout vec3 prec,vec3 val)
{
    float t = time;
    p.x+=sin(t*2.0+p.y*60.0)*0.02;
    ori(p,c);
    prec+=c*val*0.2*(abs(sin(t*0.3))-1.2);
    prec+=cos(t*-80.0+p.y*80.0)*0.2;
    prec+=cos(t*5.0+p.y*20.0)*0.05;
}

void main(){   
    vec2 p = (gl_FragCoord.xy * 2.0 - resolution.xy) / min(resolution.x, resolution.y);
    ori(p,c);
    fil(p+0.02,c,vec3(1.0,0.0,0.0));
    fil(p-0.02,c,vec3(0.0,0.0,1.0));

    gl_FragColor = vec4(c, 1.0);
}