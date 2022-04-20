# McCulloch-Pitts

1. The activation of a McCulloch-Pitts neuron is binary. That is, at any time
step, the neuron either fires (has an activation of 1) or does not fire (has an
activation of 0).
2. McCulloch-Pitts neurons are connected by directed, weighted paths.
3. A connection path is excitatory if the weight on the path is positive; other-
wise it is inhibitory. All excitatory connections into a particular neuron have
the same weights.
4. Each neuron has a fixed threshold such that if the net input to the neuron
is greater than the threshold, the neuron fires.
5. The threshold is set so that inhibition is absolute. That is, any nonzero
inhibitory input will prevent the neuron from firing.
6. It takes one time step for a signal to pass over one connection link.
--------------------------------------------------------
--------------------------------------------------------


# Hebb Net

The earliest and simplest learning rule for a neural net is generally known as the
Hebb rule.

## Algorithm:

_Step 0._
Initialize all weights:

            w(i) = 0   (i = 1 to n).
_Step 1._
 For each input training vector and target output pair,

        s : t, do steps 2-4.

_Step 2._
Set activations for input units:

            x(i) = s(i)    (i = 1 to n).

_Step 3._
Set activation for output unit:
        
            y = t.

_Step 4._
Adjust the weights for

            w(i)(new) = w(i)(old) + x(i)*y  (i = 1 to n).
 Adjust the bias:
 
            b(new) = b(old) + y.
--------------------------------------------------------
--------------------------------------------------------
# ADALINE

An **ADALINE** is a single unit (neuron) that receives input from several units. It
also receives input from a "unit" whose signal is always + 1, in order for the bias
weight to be trained by the same process (the delta rule) as is used to train the
other weights.

![adaline](https://i2.wp.com/www.mlopt.com/wp-content/uploads/2016/06/Figure2.png?resize=445%2C320)

## Algorithm:

_Step 0._

        Initialize weights. (Small random values are usually used.)
        Set learning rate a.

_Step 1._

        While stopping condition is false, do Steps 2-6

_Step 2._
For each bipolar training pair

         s:t, do Steps 3-5.

_Step 3._
Set activations of input units

        x(i) = s(i). i = 1, . . . , n:

_Step 4._
Compute net input to output unit:

        y_in = b + Sigma(x(i) * w(i)).

_Step 5._
Update bias and weights, 

        b(new) = b(old) + a(t — y_in).
        w(i)(new) = w(i)(old) + a(t — y_in)x(i).
        i = 1, . . . , n:

_Step 6._
Test for stopping condition:
        
        If the largest weight change that occurred in Step 2 is
        smaller than a specified tolerance, then stop; otherwise continue.
--------------------------------------------------------
--------------------------------------------------------
# MADALINE
**MADALINE** consists of Many **Adaptive Linear Neurons** arranged in a multilayer net.

![madaline](https://www.pyimagedata.com/wp-content/uploads/2020/10/image-23.png)

## Training Algorithm for MADALINE
z1 and z2 are in hidden layer and Y is in output layer;
The activation function is **Sign function**:

![sign function](https://static.wixstatic.com/media/884a24_b2d44f33d5324bdf8d2467c7d5ad4e03~mv2.png/v1/fill/w_700,h_378,al_c,lg_1/884a24_b2d44f33d5324bdf8d2467c7d5ad4e03~mv2.png)

## Algorithm:
_step 0._
Initialize weights:

        Weights v i and v2 and the bias b3 are set as described;
small random values are usually used for ADALINE weights.
Set the learning rate alpha as in the ADALINE training algorithm (a small
value)
 _step 1._
 While stopping condition is false
 
         do Steps 2-8.
    
_step 2._
For each bipolar training pair
        
         s:t, do Steps 3-7.
         
_step 3._
Set activations of input units:
        
        x(i) = S(i)
        
_step 4._
Compute net input to each hidden ADALINE unit:

        z_in1 = b(1) + x(1)w(11) + x(2)w(21)
        z_in2 = b(2) + x(1)w(12) + x(2)w(22)

_step 5._
Determine output of each hidden ADALINE unit:

        z1 = f(z_in1)
        z2 = f(z_in2)

_step 6._
etermine output of net:

        y_in = b(3) + z1*v1 + z2*v2
        y = f(y_in).

_step 7._
Determine error and update weights:
If t = y

        no weight updates are performed.
Otherwise:
If t = 1

        then update weights on z(j)
        the unit whose net input is closest to 0,
        b(j)(new) = b(1)(old) + a(1 — z_in(j))
        w(ij)(new) = w(if)(old) + a(1 — z_in(j))x(i0 
If t = —1

        then update weights on all units
        z(k) that have positive net input,
        b(k)(new) = b(k)(old) + a( — 1 — z—ink),
        w(ik)(new) = w(ik)(old) + a( — 1 — z_ink)xi

_step 8._
Test stopping condition.

        If weight changes have stopped (or reached an acceptable
        level), or if a specified maximum number of weight update
        iterations (Step 2) have been performed, then stop
otherwise continue.

--------------------------------------------------------
--------------------------------------------------------
# Perceptron
**Perceptrons** had perhaps the most far-reaching impact of any of the early neural nets. 
The perceptron learning rule is a more powerful learning rule than the Hebb rule.

The activation function for each associator unit was the binary step function
with an arbitrary, but fixed, threshold. Thus, the signal sent from the associator units to the output unit was a binary (0 or 1) signal. 
The output of the perceptron is y = f(y_in), where the activation function is like sign function with threshold.

## Algorithm:

_step 0._
Initialize weights and bias.

        (For simplicity, set weights and bias to zero.)
        Set learning rate a (0 < a < 1).
        (For simplicity, a can be set to 1.)
While stopping condition is false,

        do Steps 2-6.
_Step 2._
For each training pair

        s:t, do Steps 3-5.
_Step 3._
Set activations of input units:

        x(i) = S(i).
_Step 4._
Compute response of output unit:

        y_in = b + sigma(x(i)w(i));
        activation function.
        
_Step 5._
Update weights and bias if an error occurred for this pattern.
If y = t,

        w(i)(new) = w(i)(old) + a*t*x(i),
        b(new) = b(old) + a*t
else

        w(i)(new) = w(i)(old),
        b(new) =  b(old).
Step 6.
Test stopping condition:

        If no weights changed in Step 2, stop; else, continue.
        
--------------------------------------------------------
--------------------------------------------------------
