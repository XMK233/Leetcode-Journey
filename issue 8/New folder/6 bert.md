# 1. [bert\_cased\_L-12\_H-768\_A-12@v1](https://aihub.cloud.google.com/p/products%2F2c1fe4d8-4ff3-4d4f-8ac4-45d445532a3b)
## Overview

This module contains a deep bidirectional transformer trained on Wikipedia and
the BookCorpus. The details are described in the paper "BERT: Pre-training of
Deep Bidirectional Transformers for Language Understanding" [1].

This module assumes pre-processed inputs from the BERT repository
(https://github.com/google-research/bert)

This modules outputs a representations for every token in the input sequence and
a pooled representation of the entire input.

#### Trainable parameters

All parameters in the module are trainable, and fine-tuning all parameters is
the recommended practice.

#### Example use

Please see
https://github.com/google-research/bert/blob/master/run_classifier_with_tfhub.py
for how the input preprocessing should be done to retrieve the input ids, masks,
and segment ids.

```
bert_module = hub.Module("https://tfhub.dev/google/bert.../1", trainable=True)
bert_inputs = dict(
    input_ids=input_ids,
    input_mask=input_mask,
    segment_ids=segment_ids)
bert_outputs = bert_module(bert_inputs, signature="tokens", as_dict=True)
pooled_output = bert_outputs["pooled_output"]
sequence_output = bert_outputs["sequence_output"]
```

The pooled_output is a `[batch_size, hidden_size]` Tensor. The sequence_output
is a `[batch_size, sequence_length, hidden_size]` Tensor.

### Inputs

We currently only support the `tokens` signature, which assumes pre-processed
inputs. `input_ids`, `input_mask`, and `segment_ids` are `int32` Tensors of
shape `[batch_size, max_sequence_length]`

### Outputs

The output dictionary contains:

*   `pooled_output`: pooled output of the entire sequence with shape
    `[batch_size, hidden_size]`.
*   `sequence_output`: representations of every token in the input sequence with
    shape `[batch_size, max_sequence_length, hidden_size]`.

## Changelog

#### Version 1

*   Initial release.

#### References

[1] Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova. [BERT:
Pre-training of Deep Bidirectional Transformers for Language
Understanding](https://arxiv.org/abs/1810.04805). arXiv preprint
arXiv:1810.04805, 2018.
---------
# 2. [bert\_cased\_L-24\_H-1024\_A-16@v1](https://aihub.cloud.google.com/p/products%2Fadd1e4fb-a853-4a8e-96e4-e2a5b470438f)
## Overview

This module contains a deep bidirectional transformer trained on Wikipedia and
the BookCorpus. The details are described in the paper "BERT: Pre-training of
Deep Bidirectional Transformers for Language Understanding" [1].

This module assumes pre-processed inputs from the BERT repository
(https://github.com/google-research/bert)

This modules outputs a representations for every token in the input sequence and
a pooled representation of the entire input.

#### Trainable parameters

All parameters in the module are trainable, and fine-tuning all parameters is
the recommended practice.

#### Example use

Please see
https://github.com/google-research/bert/blob/master/run_classifier_with_tfhub.py
for how the input preprocessing should be done to retrieve the input ids, masks,
and segment ids.

```
bert_module = hub.Module("https://tfhub.dev/google/bert.../1", trainable=True)
bert_inputs = dict(
    input_ids=input_ids,
    input_mask=input_mask,
    segment_ids=segment_ids)
bert_outputs = bert_module(bert_inputs, signature="tokens", as_dict=True)
pooled_output = bert_outputs["pooled_output"]
sequence_output = bert_outputs["sequence_output"]
```

The pooled_output is a `[batch_size, hidden_size]` Tensor. The sequence_output
is a `[batch_size, sequence_length, hidden_size]` Tensor.

### Inputs

We currently only support the `tokens` signature, which assumes pre-processed
inputs. `input_ids`, `input_mask`, and `segment_ids` are `int32` Tensors of
shape `[batch_size, max_sequence_length]`

### Outputs

The output dictionary contains:

*   `pooled_output`: pooled output of the entire sequence with shape
    `[batch_size, hidden_size]`.
*   `sequence_output`: representations of every token in the input sequence with
    shape `[batch_size, max_sequence_length, hidden_size]`.

## Changelog

#### Version 1

*   Initial release.

#### References

[1] Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova. [BERT:
Pre-training of Deep Bidirectional Transformers for Language
Understanding](https://arxiv.org/abs/1810.04805). arXiv preprint
arXiv:1810.04805, 2018.
---------
# 3. [bert\_chinese\_L-12\_H-768\_A-12@v1](https://aihub.cloud.google.com/p/products%2Ff28d5f8a-0fa9-4f79-b70f-da39924c3c9b)
## Overview

This module contains a deep bidirectional transformer trained on Wikipedia and
the BookCorpus. The details are described in the paper "BERT: Pre-training of
Deep Bidirectional Transformers for Language Understanding" [1].

This module assumes pre-processed inputs from the BERT repository
(https://github.com/google-research/bert)

This modules outputs a representations for every token in the input sequence and
a pooled representation of the entire input.

#### Trainable parameters

All parameters in the module are trainable, and fine-tuning all parameters is
the recommended practice.

#### Example use

Please see
https://github.com/google-research/bert/blob/master/run_classifier_with_tfhub.py
for how the input preprocessing should be done to retrieve the input ids, masks,
and segment ids.

```
bert_module = hub.Module("https://tfhub.dev/google/bert.../1", trainable=True)
bert_inputs = dict(
    input_ids=input_ids,
    input_mask=input_mask,
    segment_ids=segment_ids)
bert_outputs = bert_module(bert_inputs, signature="tokens", as_dict=True)
pooled_output = bert_outputs["pooled_output"]
sequence_output = bert_outputs["sequence_output"]
```

The pooled_output is a `[batch_size, hidden_size]` Tensor. The sequence_output
is a `[batch_size, sequence_length, hidden_size]` Tensor.

### Inputs

We currently only support the `tokens` signature, which assumes pre-processed
inputs. `input_ids`, `input_mask`, and `segment_ids` are `int32` Tensors of
shape `[batch_size, max_sequence_length]`

### Outputs

The output dictionary contains:

*   `pooled_output`: pooled output of the entire sequence with shape
    `[batch_size, hidden_size]`.
*   `sequence_output`: representations of every token in the input sequence with
    shape `[batch_size, max_sequence_length, hidden_size]`.

## Changelog

#### Version 1

*   Initial release.

#### References

[1] Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova. [BERT:
Pre-training of Deep Bidirectional Transformers for Language
Understanding](https://arxiv.org/abs/1810.04805). arXiv preprint
arXiv:1810.04805, 2018.
---------
# 4. [bert\_multi\_cased\_L-12\_H-768\_A-12@v1](https://aihub.cloud.google.com/p/products%2F9673daa5-5abe-41e6-9392-7feae1ce56fc)
## Overview

This module contains a deep bidirectional transformer trained on Wikipedia and
the BookCorpus. The details are described in the paper "BERT: Pre-training of
Deep Bidirectional Transformers for Language Understanding" [1].

This module assumes pre-processed inputs from the BERT repository
(https://github.com/google-research/bert)

This modules outputs a representations for every token in the input sequence and
a pooled representation of the entire input.

#### Trainable parameters

All parameters in the module are trainable, and fine-tuning all parameters is
the recommended practice.

#### Example use

Please see
https://github.com/google-research/bert/blob/master/run_classifier_with_tfhub.py
for how the input preprocessing should be done to retrieve the input ids, masks,
and segment ids.

```
bert_module = hub.Module("https://tfhub.dev/google/bert.../1", trainable=True)
bert_inputs = dict(
    input_ids=input_ids,
    input_mask=input_mask,
    segment_ids=segment_ids)
bert_outputs = bert_module(bert_inputs, signature="tokens", as_dict=True)
pooled_output = bert_outputs["pooled_output"]
sequence_output = bert_outputs["sequence_output"]
```

The pooled_output is a `[batch_size, hidden_size]` Tensor. The sequence_output
is a `[batch_size, sequence_length, hidden_size]` Tensor.

### Inputs

We currently only support the `tokens` signature, which assumes pre-processed
inputs. `input_ids`, `input_mask`, and `segment_ids` are `int32` Tensors of
shape `[batch_size, max_sequence_length]`

### Outputs

The output dictionary contains:

*   `pooled_output`: pooled output of the entire sequence with shape
    `[batch_size, hidden_size]`.
*   `sequence_output`: representations of every token in the input sequence with
    shape `[batch_size, max_sequence_length, hidden_size]`.

## Changelog

#### Version 1

*   Initial release.

#### References

[1] Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova. [BERT:
Pre-training of Deep Bidirectional Transformers for Language
Understanding](https://arxiv.org/abs/1810.04805). arXiv preprint
arXiv:1810.04805, 2018.
---------
# 5. [bert\_uncased\_L-12\_H-768\_A-12@v1](https://aihub.cloud.google.com/p/products%2Fac1806a5-a32c-4adf-b069-074156efc5c3)
## Overview

This module contains a deep bidirectional transformer trained on Wikipedia and
the BookCorpus. The details are described in the paper "BERT: Pre-training of
Deep Bidirectional Transformers for Language Understanding" [1].

This module assumes pre-processed inputs from the BERT repository
(https://github.com/google-research/bert)

This modules outputs a representations for every token in the input sequence and
a pooled representation of the entire input.

#### Trainable parameters

All parameters in the module are trainable, and fine-tuning all parameters is
the recommended practice.

#### Example use

Please see
https://github.com/google-research/bert/blob/master/run_classifier_with_tfhub.py
for how the input preprocessing should be done to retrieve the input ids, masks,
and segment ids.

```
bert_module = hub.Module("https://tfhub.dev/google/bert.../1", trainable=True)
bert_inputs = dict(
    input_ids=input_ids,
    input_mask=input_mask,
    segment_ids=segment_ids)
bert_outputs = bert_module(bert_inputs, signature="tokens", as_dict=True)
pooled_output = bert_outputs["pooled_output"]
sequence_output = bert_outputs["sequence_output"]
```

The pooled_output is a `[batch_size, hidden_size]` Tensor. The sequence_output
is a `[batch_size, sequence_length, hidden_size]` Tensor.

### Inputs

We currently only support the `tokens` signature, which assumes pre-processed
inputs. `input_ids`, `input_mask`, and `segment_ids` are `int32` Tensors of
shape `[batch_size, max_sequence_length]`

### Outputs

The output dictionary contains:

*   `pooled_output`: pooled output of the entire sequence with shape
    `[batch_size, hidden_size]`.
*   `sequence_output`: representations of every token in the input sequence with
    shape `[batch_size, max_sequence_length, hidden_size]`.

## Changelog

#### Version 1

*   Initial release.

#### References

[1] Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova. [BERT:
Pre-training of Deep Bidirectional Transformers for Language
Understanding](https://arxiv.org/abs/1810.04805). arXiv preprint
arXiv:1810.04805, 2018.
---------
# 6. [bert\_uncased\_L-24\_H-1024\_A-16@v1](https://aihub.cloud.google.com/p/products%2F46b652ee-80d4-4bcd-b707-1e4dcdd88759)
## Overview

This module contains a deep bidirectional transformer trained on Wikipedia and
the BookCorpus. The details are described in the paper "BERT: Pre-training of
Deep Bidirectional Transformers for Language Understanding" [1].

This module assumes pre-processed inputs from the BERT repository
(https://github.com/google-research/bert)

This modules outputs a representations for every token in the input sequence and
a pooled representation of the entire input.

#### Trainable parameters

All parameters in the module are trainable, and fine-tuning all parameters is
the recommended practice.

#### Example use

Please see
https://github.com/google-research/bert/blob/master/run_classifier_with_tfhub.py
for how the input preprocessing should be done to retrieve the input ids, masks,
and segment ids.

```
bert_module = hub.Module("https://tfhub.dev/google/bert.../1", trainable=True)
bert_inputs = dict(
    input_ids=input_ids,
    input_mask=input_mask,
    segment_ids=segment_ids)
bert_outputs = bert_module(bert_inputs, signature="tokens", as_dict=True)
pooled_output = bert_outputs["pooled_output"]
sequence_output = bert_outputs["sequence_output"]
```

The pooled_output is a `[batch_size, hidden_size]` Tensor. The sequence_output
is a `[batch_size, sequence_length, hidden_size]` Tensor.

### Inputs

We currently only support the `tokens` signature, which assumes pre-processed
inputs. `input_ids`, `input_mask`, and `segment_ids` are `int32` Tensors of
shape `[batch_size, max_sequence_length]`

### Outputs
The output dictionary contains:

*   `pooled_output`: pooled output of the entire sequence with shape
    `[batch_size, hidden_size]`.
*   `sequence_output`: representations of every token in the input sequence with
    shape `[batch_size, max_sequence_length, hidden_size]`.

## Changelog

#### Version 1
*  Initial release.

#### References

[1] Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova. [BERT:
Pre-training of Deep Bidirectional Transformers for Language
Understanding](https://arxiv.org/abs/1810.04805). arXiv preprint
arXiv:1810.04805, 2018.
---------
